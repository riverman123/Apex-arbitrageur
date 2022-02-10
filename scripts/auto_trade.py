from brownie import  *
from web3.main import Web3
import os
import time,math
from scripts import amm, router, priceOracle,margin , config_contract
from config import config
# from contract_helper import margin_test,priceOracle_test,router_test,amm,config_test
from trade_test import trade_fee


from dotenv import load_dotenv
load_dotenv()

PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key= PRIVATE_KEY_USER)
userRobert = accounts.add(private_key= PRIVATE_KEY_ROBOT )

SETTING = config.SETTING
address = config.AMM_CONTRACT_INFO["CONTRACT_ADDRESS"]
TOKEN_INFO = config.TOKEN_INFO


def auto_trade_slow(side,margin_mount=1,quote_size=10000):
    for i in range(100):
        tx_hash_openPosition = router.openPositionRouter(side=side, marginAmount=margin_mount, quoteAmount=quote_size,trader=SETTING["ADDRESS_ROBOT"],deadline=1957515898, baseToken=TOKEN_INFO["mockWETH"], quoteToken=TOKEN_INFO["mockUSDC"])
        print(tx_hash_openPosition)
        position_info = margin.getPosition(SETTING["ADDRESS_ROBOT"])
        quote_amount = position_info[1]
        mark_price = priceOracle.getMarkPrice(address=address)
        index_price = priceOracle.getIndexPrice(address=address)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) >= 0.1:
            break
    print(">>>>>>>>>>>>>>>>Start to close the position>>>>>>>>>>>>>>>")
    for i in range(abs(int(quote_amount / (10000 * (10 ** 6))))):
        margin.closePosition(trader=SETTING["ADDRESS_ROBOT"], quoteAmount=quote_size)
        margin.getPosition(SETTING["ADDRESS_ROBOT"])
        mark_price = priceOracle.getMarkPrice(address=address)
        index_price = priceOracle.getIndexPrice(address=address)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) <= -0.1:
            break
    return_margin(SETTING["ADDRESS_ROBOT"])

def return_margin(trader):
    user_wthdrawAble = margin.getWithdrawable(trader)
    margin.removeMargin(trader=trader,withdrawAmount=user_wthdrawAble)

def get_max_position(margin_amount,margin_rate):
    beta = config_contract.getBeta()
    reserves = amm.getReserves(is_print=False)
    amm_y_first = reserves[1]
    print(amm_y_first)
    market_price = reserves[1] / reserves[0] * (10 ** 12)
    v_1 = margin_rate/(margin_amount*market_price)
    v_2 = 2*beta/(amm_y_first/(10**6))
    v_3 = -1/(v_1+v_2)
    return v_3

# 使用机器人砸低市价
def price_increase(target_price,market_price,side):
    reserves = amm.getReserves()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = (amm_x/(10**18))*(amm_y/(10**6))
    quote_amount = math.sqrt(amm_l)*(math.sqrt(target_price)-math.sqrt(market_price))
    router.openPositionRouter(side=side, marginAmount=20000, quoteAmount=int(abs(quote_amount)) + 1,trader=SETTING["ADDRESS_ROBOT"])
    
    position_info = margin.getPosition(trader=SETTING["ADDRESS_ROBOT"])
    print("机器人仓位：",position_info)
    return position_info

def get_amml():
    reserves = amm.getReservesAccurate()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = 1.0*amm_x*amm_y/(10**24)
    return abs(amm_l)

# 清算用户仓位
def liquidate(trader):
    debt_ratio = margin.getDebtRatio(trader)
    print('debt_ratio:',debt_ratio)
    # if debt_ratio > 10000:
    print('>>>>>>begin liquidate')
    return margin.toliquidate(trader=trader)

def get_margin_acc(quoteAmount,vUSD,market_price):
    beta = config_contract.getBeta()
    v_1 = 2.0*beta/vUSD
    v_2 = 1/((1/quoteAmount-v_1)*market_price*10)
    return abs(v_2)

# 计算仓位的清算价格
def get_liquidate_price(trader):
    beta = config_contract.getBeta()
    position_info = margin.getPositionAccurate(trader)
    amm_l = get_amml()
    v_1 = (position_info[1]**2)/(4*amm_l)/(10**12)
    v_2 = position_info[1]/(position_info[0]+margin.getFundingAccurate(trader))*(10**12)
    v_3 = math.sqrt(v_1-v_2)-beta*(position_info[1]/math.sqrt(amm_l))/(10**6)
    print("清算价格: ",v_3*v_3)
    liquidate_price = v_3*v_3
    return liquidate_price


# check amm
def check_liquidate():
    percent_list = [0.01,0.02,0.04,0.06,0.08,0.1,0.12,0.14]
    # percent_list = [0.01]
    for i in percent_list:
        print('>>>>>>>>>>>>>>>>>>>>>>>开仓量为总流动行性的%f'%i,'>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # 检查Amm池子的状况
        base_reserves_begin = amm.getReservesAccurate()[0]
        reserves = amm.getReserves(is_print=True)
        amm_x_first = reserves[0]
        amm_y_first = reserves[1]
        amm_l = get_amml()
        # 计算当前价格
        market_price = reserves[1]/reserves[0]*(10**12)
        print("market_price:",market_price)
        # 使用用户A10倍杠杆开多
        # marginAmount = round(amm_x_first*i/(10**21),2)
        quoteAmount = int(abs(math.sqrt(amm_l)*i))
        marginAmount = round(get_margin_acc(quoteAmount,amm_y_first/(10**6),market_price),2)
        print("margin:",marginAmount,"    quote_size:",quoteAmount)
        router.openPositionRouter(side=0, marginAmount=marginAmount, quoteAmount=quoteAmount,trader=SETTING["ADDRESS_USER"])
        print("用户A仓位:",margin.getPosition(SETTING["ADDRESS_USER"]))
        time.sleep(5)
        # 检查Amm池子的状况
        reserves =  amm.getReserves(is_print=True)
        # 计算当前价格
        market_price = reserves[1]/reserves[0]*(10**12)
        print("用户A开仓后的market_price：",market_price)
        # 计算用户A的清算价格
        target_price = get_liquidate_price(trader=SETTING["ADDRESS_USER"])
        # 将场内价格砸至用户a的清算价格
        price_increase(target_price=abs(target_price),market_price=abs(market_price),side=1)
        # 将用户A的仓位清算
        tx = liquidate(trader=SETTING["ADDRESS_USER"])
        #todo calculate the fee
        #liquidate_fee = trade_fee.get_trade_fee(tx_id=tx,is_liquidate=True)*0.001
        # 检查Amm池子的状况
        # amm.getReserves(is_print=True)
        # 将机器人的仓位平仓
        quoteAmount = margin.getPositionAccurate(trader=SETTING["ADDRESS_ROBOT"])[1]
        tx = margin.closePosition(trader=SETTING["ADDRESS_ROBOT"],quoteAmount=abs(quoteAmount))
        #close_position_fee = trade_fee.get_trade_fee(tx_id=tx,is_liquidate=False)
        # 检查Amm池子的状况
        reserves_end = amm.getReserves(is_print=True)
        amm_x_end = reserves_end[0]
        amm_y_end = reserves_end[1]
        print("池子X的变化：",(amm_x_end-amm_x_first)/(10**18))
        print("池子y的变化：",(amm_y_end-amm_y_first)/(10**6))
        return_margin(SETTING["ADDRESS_USER"],SETTING["PRIVATE_KEY_USER"])
        return_margin(SETTING["ADDRESS_ROBOT"],SETTING["PRIVATE_KEY_ROBOT"])
        amm.setBaseReserve(base_reserves_begin)
        amm.rebaseFree()




def main():
    check_liquidate()
    #print(get_amml())

    # get_liquidate_price(trader=SETTING["ADDRESS_USER"], beta=1)
