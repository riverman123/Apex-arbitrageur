import time,math

from config import config
import margin_test,priceOracle_test,router_test,amm_test
from web3.main import Web3

SETTING = config.SETTING
w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
address = config.AMM_CONTRACT_INFO["CONTRACT_ADDRESS"]
TOKEN_INFO = config.TOKEN_INFO

def auto_trade_slow(side,margin_mount=1,quote_size=10000):
    for i in range(100):
        tx_hash_openPosition = router_test.openPositionRouter(side=side, marginAmount=margin_mount, quoteAmount=quote_size,trader=SETTING["ADDRESS_ROBOT"],trader_key=SETTING["PRIVATE_KEY_ROBOT"],deadline=1957515898, baseToken=TOKEN_INFO["mockWETH"], quoteToken=TOKEN_INFO["mockUSDC"])
        print(tx_hash_openPosition.hex())
        # Wait for the transaction result to be confirmed
        w3.eth.waitForTransactionReceipt(tx_hash_openPosition)
        position_info = margin_test.getPosition(SETTING["ADDRESS_ROBOT"])
        quote_amount = position_info[1]
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) >= 0.1:
            break
    print(">>>>>>>>>>>>>>>>Start to close the position>>>>>>>>>>>>>>>")
    for i in range(abs(int(quote_amount / (10000 * (10 ** 6))))):
        tx_hash_closePosition = margin_test.closePosition(trader=SETTING["ADDRESS_ROBOT"], quoteAmount=quote_size)
        print(tx_hash_closePosition.hex())
        w3.eth.waitForTransactionReceipt(tx_hash_closePosition)
        margin_test.getPosition(SETTING["ADDRESS_ROBOT"])
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) <= -0.1:
            break
    return_margin(SETTING["ADDRESS_ROBOT"])

def quick_increase():
    for i in range(10):
        tx_hash_openPosition = router_test.openPositionRouter(side=0, marginAmount=30, quoteAmount=500000)
        print(tx_hash_openPosition.hex())
        # Wait for the transaction result to be confirmed
        w3.eth.waitForTransactionReceipt(tx_hash_openPosition)
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        print("mark_price：", mark_price)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) >= 0.1:
            break
    position_info = margin_test.getPosition(SETTING["ADDRESS_ROBOT"])
    margin_test.closePosition(trader=SETTING["ADDRESS_ROBOT"],
                              quoteAmount=abs(int(position_info[1] / (10 ** 6))))

def quick_reduce():
    for i in range(10):
        tx_hash_openPosition = router_test.openPositionRouter(side=1, marginAmount=300, quoteAmount=500000)
        print(tx_hash_openPosition.hex())
        # Wait for the transaction result to be confirmed
        w3.eth.waitForTransactionReceipt(tx_hash_openPosition)
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        print("mark_price：", mark_price)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) <= -0.1:
            break
    position_info = margin_test.getPosition(SETTING["ADDRESS_ROBOT"])
    margin_test.closePosition(trader=SETTING["ADDRESS_ROBOT"],
                              quoteAmount=abs(int(position_info[1] / (10 ** 6))))

def return_margin(trader):
    user_wthdrawAble = margin_test.getWithdrawable(trader)
    margin_test.removeMargin(trader=trader,withdrawAmount=user_wthdrawAble)

# 使用机器人砸低市价
def price_increase(target_price,market_price,side):
    reserves = amm_test.getReserves()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = (amm_x/(10**18))*(amm_y/(10**6))
    quote_amount = math.sqrt(amm_l)*(math.sqrt(target_price)-math.sqrt(market_price))
    tx_hash_openPosition=router_test.openPositionRouter(side=side, marginAmount=2000, quoteAmount=int(abs(quote_amount)) + 1,trader=SETTING["ADDRESS_ROBOT"],trader_key=SETTING["PRIVATE_KEY_ROBOT"])
    w3.eth.waitForTransactionReceipt(tx_hash_openPosition.hex())
    print("机器人仓位：")
    margin_test.getPosition(trader=SETTING["ADDRESS_ROBOT"])
    return tx_hash_openPosition.hex()

def get_amml():
    reserves = amm_test.getReserves()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = (amm_x/(10**18))*(amm_y/(10**6))
    return abs(amm_l)

# 清算用户仓位
def liquidate(trader,trader_key):
    debt_ratio = margin_test.getDebtRatio(trader)
    print('debt_ratio:',debt_ratio)
    # if debt_ratio > 10000:
    print('>>>>>>>>>>>>begin liquidate>>>>>>>>>>>')
    margin_test.toliquidate(trader=trader,trader_key=trader_key)

# 计算仓位的清算价格
def get_liquidate_price(trader,beta):
    print("用户A仓位：")
    position_info = margin_test.getPosition(trader)
    amm_l = get_amml()
    v_1 = (position_info[1]**2)/(4*amm_l)
    v_2 = position_info[1]/(position_info[0]+margin_test.getFunding(trader))
    print("v2:",v_2)
    v_3 = math.sqrt(v_1-v_2)-beta*(position_info[1]/math.sqrt(amm_l))
    # print("math.sqrt(v_1-v_2):",math.sqrt(v_1-v_2))
    # print("math.sqrt(amm_l):",math.sqrt(amm_l))
    # print("式子的第二项：",position_info[1]/math.sqrt(amm_l))
    liquidate_price = v_3*v_3
    # print(liquidate_price)
    # 暂时return V_2，v_2与页面清算价格一致
    return v_2


# check amm
def check_liquidate():
    # 检查Amm池子的状况
    reserves = amm_test.getReserves(is_print=True)
    # 计算当前价格
    market_price = reserves[1]/reserves[0]*(10**12)
    print("market_price:",market_price)
    # 使用用户A10倍杠杆开多
    router_test.openPositionRouter(side=0, marginAmount=1, quoteAmount=int(abs(market_price)*10),trader=SETTING["ADDRESS_USER"],trader_key=SETTING["PRIVATE_KEY_USER"])
    # 检查Amm池子的状况
    reserves =  amm_test.getReserves(is_print=True)
    # 计算当前价格
    market_price = reserves[1]/reserves[0]*(10**12)
    # 计算用户A的清算价格
    target_price = get_liquidate_price(trader=SETTING["ADDRESS_USER"],beta=1)
    # 将场内价格砸至用户a的清算价格
    price_increase(target_price=abs(target_price),market_price=abs(market_price),side=1)
    # 将用户A的仓位平仓
    liquidate(trader=SETTING["ADDRESS_USER"],trader_key=SETTING["PRIVATE_KEY_USER"])
    # 检查Amm池子的状况
    amm_test.getReserves(is_print=True)
    # 将机器人的仓位平仓
    quoteAmount = margin_test.getPositionAccurate(trader=SETTING["ADDRESS_ROBOT"])[1]
    margin_test.closePosition(trader=SETTING["ADDRESS_ROBOT"],trader_key=SETTING["PRIVATE_KEY_ROBOT"],quoteAmount=abs(quoteAmount))
    # 检查Amm池子的状况
    amm_test.getReserves(is_print=True)



if __name__ == '__main__':
    check_liquidate()
