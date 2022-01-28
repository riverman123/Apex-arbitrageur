import time,math

from config import config
import margin_test,priceOracle_test,router_test,amm_test
from web3.main import Web3

SETTING = config.SETTING
w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
address = config.AMM_CONTRACT_INFO["CONTRACT_ADDRESS"]
xz
def auto_trade_slow(side,margin_mount,quote_size):
    for i in range(100):
        tx_hash_openPosition = router_test.openPositionRouter(side=side, marginAmount=margin_mount, quoteAmount=quote_size)
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

def price_increase(target_price,market_price,side):
    reserves = amm_test.getReserves()
    amm_x = reserves[0]
    amm_y = reserves[1]
    amm_l = (amm_x/(10**18))*(amm_y/(10**6))
    quote_amount = math.sqrt(amm_l)*(math.sqrt(target_price)-math.sqrt(market_price))
    tx_hash_openPosition=router_test.openPositionRouter(side=side, marginAmount=2000, quoteAmount=int(abs(quote_amount)) + 1)
    w3.eth.waitForTransactionReceipt(tx_hash_openPosition.hex())
    return tx_hash_openPosition.hex()

def liquidate(trader):
    debt_ratio = margin_test.getDebtRatio(trader)
    print('debt_ratio:',debt_ratio)
    # if debt_ratio > 10000:
    print('>>>>>>>>>>>begain liquidate>>>>>>>>>>')
    margin_test.toliquidate(trader)
    amm_test.getReserves()

if __name__ == '__main__':

    # print(math.sqrt(36711223916.563805)*(math.sqrt(75.75)-math.sqrt(83.22)))
    # tx_hash_openPosition=router_test.openPositionWeth(side=1, marginAmount=1000, quoteAmount=80291)
    # print(tx_hash_openPosition.hex())
    # time.sleep(2)
    # date=w3.eth.getTransactionReceipt(tx_hash_openPosition.hex())
    # returnData = date["returnData"]
    # print(Web3.toText(hexstr=returnData[10:]))
    price_increase(target_price=75.83,market_price=83.38,side=1)
    liquidate('0x6014F6D866F3EeC7463c7D74639185265a98C91D')
    quote_size = margin_test.getPosition(trader=SETTING["WALLET_ADDRESS"])[1]
    margin_test.closePosition(trader=SETTING["WALLET_ADDRESS"],quoteAmount=quote_size)
    amm_test.getReserves()



