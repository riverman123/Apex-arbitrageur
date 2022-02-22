import os
import math,time
from brownie import *
from dotenv import load_dotenv

from scripts import amm, router, priceOracle,margin , config_contract,trade_fee
from config import config
from database import amm_profit_loss


load_dotenv()

PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key=PRIVATE_KEY_USER)
userRobert = accounts.add(private_key=PRIVATE_KEY_ROBOT)

SETTING = config.SETTING
address = config.AMM_CONTRACT_INFO["CONTRACT_ADDRESS"]
TOKEN_INFO = config.TOKEN_INFO


def get_max_position(margin_amount, margin_rate):
    beta = config_contract.getBeta()
    reserves = amm.getReserves(is_print=False)
    amm_y_first = reserves[1]
    print(amm_y_first)
    market_price = reserves[1] / reserves[0] * (10 ** 12)
    v_1 = margin_rate / (margin_amount * market_price)
    v_2 = 2 * beta / (amm_y_first / (10 ** 6))
    v_3 = -1 / (v_1 + v_2)
    return v_3


# 使用机器人砸低市价
def calculate_liquidate_price_and_open_position(target_price, market_price, side):
    reserves = amm.getReserves()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = (amm_x / (10 ** 18)) * (amm_y / (10 ** 6))
    if side == 0:
        quote_amount = math.sqrt(amm_l) * (math.sqrt(target_price) - math.sqrt(market_price))
        robot_open_tx = router.openPositionRouter(side=1, marginAmount=20000,
                                                  quoteAmount=int(abs(quote_amount)) + 1,
                                                  trader=SETTING["ADDRESS_ROBOT"],
                                                  )
        position_info = margin.getPosition(trader=SETTING["ADDRESS_ROBOT"])
        print("机器人仓位：", position_info)
        print("当前的MarkPrice:", priceOracle.getMarkPrice())
    else:
        quote_amount = math.sqrt(amm_l) * (math.sqrt(market_price) - math.sqrt(target_price))
        robot_open_tx = router.openPositionRouter(side=0, marginAmount=20000,
                                                  quoteAmount=int(abs(quote_amount)) + 1,
                                                  trader=SETTING["ADDRESS_ROBOT"],
                                                  )
        position_info = margin.getPosition(trader=SETTING["ADDRESS_ROBOT"])
        print("机器人仓位：", position_info)
        print("当前的MarkPrice:", priceOracle.getMarkPrice())
    return [robot_open_tx,position_info]


def get_amml():
    reserves = amm.getReservesAccurate()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = 1.0 * amm_x * amm_y / (10 ** 24)
    return abs(amm_l)


# liquidate user A position when it's debt_ratio >= 99.8%
def liquidate(trader):
    debt_ratio = margin.getDebtRatio(trader)
    print('debt_ratio:', debt_ratio)
    print('>>>>>>begin liquidate>>>>>>')
    hash_tx = margin.toliquidate(trader=trader)
    return [hash_tx,debt_ratio]


def get_margin_acc(quoteAmount, vUSD, market_price):
    beta = config_contract.getBeta()
    v_1 = 2.0 * beta / vUSD
    v_2 = 1 / ((1 / quoteAmount - v_1) * market_price * 10)
    return abs(v_2)


# Calculate the liquidate price of a position
def get_liquidate_price(trader):
    beta = config_contract.getBeta()
    position_info = margin.getPositionAccurate(trader)
    amm_l = get_amml()
    v_1 = (position_info[1] ** 2) / (4 * amm_l) / (10 ** 12)
    v_2 = position_info[1] / (position_info[0] + margin.calFundingFeeRaw(trader)) * (10 ** 12)
   
    temp = (position_info[1] ** 2) / (4 * amm_l) / (10 ** 12) - ( position_info[1] / (position_info[0] + margin.calFundingFeeRaw(trader)) * (10 ** 12))
   
    v_3 = math.sqrt(v_1 - v_2) - beta * (position_info[1] / math.sqrt(amm_l)) / (10 ** 6)
    liquidate_price = math.pow(math.sqrt(temp) - beta * (position_info[1] / math.sqrt(amm_l)) / (10 ** 6) ,2)
    print("清算价格: ", liquidate_price)
    return liquidate_price


# check amm profit and loss
def check_liquidate(side,beta):
    # set the beta by config contract
    config_contract.setBeta(beta)
    percent_list = [0.01,0.02,0.04,0.06,0.08,0.1,0.12,0.14]
    # percent_list = [0.04,0.14]
    beta = config_contract.getBetaRaw()
    print("beta: ", beta)
    for i in percent_list:
        print('>>>>>>>>>>>>>>>>>>>>>>>开仓量为总流动行性的%f' % i, '>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # rebase amm liquidity
        amm.rebaseFree()
        # get reserves of the amm
        reserves_begin = amm.getReserves(is_print=True)
        amm_x_first = reserves_begin[0]
        amm_y_first = reserves_begin[1]
        amm_l = get_amml()
        # get market price by priceOracle contract
        market_price_begin = priceOracle.getMarkPrice()
        print("market_price:", market_price_begin)
        quoteAmount = int(abs(math.sqrt(amm_l) * i))
        marginAmount = round(get_margin_acc(quoteAmount, amm_y_first / (10 ** 6), market_price_begin), 2)
        print("margin:", marginAmount, "    quote_size:", quoteAmount)
        # open a position with user A and Leverage nearby 10
        user_open_tx = router.openPositionRouter(side=side, marginAmount=marginAmount, quoteAmount=quoteAmount,
                                  trader=SETTING["ADDRESS_USER"])
        # get the trade fee of this time open position
        trade_fee_amount = trade_fee.get_trade_fee(tx=user_open_tx,is_liquidate=False)
        # get the position inf of the user A
        user_a_position = margin.getPosition(SETTING["ADDRESS_USER"])
        print("trade_fee A open:",trade_fee_amount/10**18)
        print("用户A仓位:",user_a_position)
        # check the amm liquidity now
        reserves = amm.getReserves(is_print=True)
        # get the market price now
        market_price_after_a = priceOracle.getMarkPrice()
        # get the liquidate price of user A's  position
        target_price = get_liquidate_price(trader=SETTING["ADDRESS_USER"])
        # use user B to open a big position make the market price nearby the liquidate price of the user A's position
        robot_open_info = calculate_liquidate_price_and_open_position(target_price=abs(target_price)*(1+0.01), market_price=abs(market_price_after_a), side=side)
        trade_fee_amount = trade_fee_amount+trade_fee.get_trade_fee(tx=robot_open_info[0],is_liquidate=False)
        market_price_after_b = priceOracle.getMarkPrice()
        print("trade_fee robot open:",trade_fee_amount/10**18)
        print("funding fee A: ", margin.calFundingFee(SETTING["ADDRESS_USER"]))

        market_price_acc = priceOracle.getMarkPriceAcc(amm.CONTRACT_INFO["CONTRACT_ADDRESS"], beta, quoteAmount , False)
        print("用户A开仓后的market_price_A：", market_price_acc)
        
        # liquidate user A's position
        liquidate_info = liquidate(trader=SETTING["ADDRESS_USER"])
        trade_fee_amount = trade_fee_amount+trade_fee.get_trade_fee(tx=liquidate_info[0],is_liquidate=True)
        print("trade_fee A liquidate:",trade_fee_amount/10**18)

        # get reserves of the amm now
        amm.getReserves(is_print=True)
        # get the position inf of user B's position
        quoteAmount = margin.getPositionAccurate(trader=SETTING["ADDRESS_ROBOT"])[1]
        print("funding fee robot: ", margin.calFundingFee(SETTING["ADDRESS_ROBOT"]))
        # close user B's position
        robot_close_tx = margin.closePosition(trader=SETTING["ADDRESS_ROBOT"], quoteAmount=abs(quoteAmount))
        trade_fee_amount = trade_fee_amount+trade_fee.get_trade_fee(tx=robot_close_tx,is_liquidate=False)
        print("trade_fee robot close:",trade_fee_amount/10**18)
        reserves_end = amm.getReserves(is_print=True)
        amm_x_end = reserves_end[0]
        profit_loss = (amm_x_end - amm_x_first - trade_fee_amount) / (10 ** 18)
        print("amm reserves base coin's variety：", (amm_x_end - amm_x_first) / (10 ** 18))
        print("the total amount trade fee：", trade_fee_amount/(10**18))
        print("amm reserves quote coin's variety：：", profit_loss)
        margin.return_margin(SETTING["ADDRESS_USER"])
        margin.return_margin(SETTING["ADDRESS_ROBOT"])
        # remake the base coin's numbers
        amm.setBaseReserve(36649871750740971435566)
        # rebase the amm's reserves inf
        amm.rebaseFree()
        # insert the records
        amm_profit_loss.insert_records(beta=config_contract.getBeta(),debt_ratio=liquidate_info[1],liquidity_ratio=i,base_reserves_begin=reserves_begin,market_price_begin=market_price_begin,user_a_position=user_a_position,liquidate_price=target_price,user_b_position=robot_open_info[1],market_price_after_b=market_price_after_b,profit_loss=profit_loss,profit_percent=profit_loss/(trade_fee_amount/(10**18)))


def main():
    # beta_list = [50,55,60,65,70,75,80,85,90,95,100]
    beta_list = [90]
    for i in beta_list:
        check_liquidate(1,i)
        time.sleep(60)


