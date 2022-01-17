from config import config
import margin_test,priceOracle_test,router_test
from web3.main import Web3


SETTING = config.SETTING
w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
address = config.AMM_CONTRACT_INFO["CONTRACT_ADDRESS"]

def auto_trade_slow():
    for i in range(100):
        tx_hash_openPosition = router_test.openPositionWeth(side=0, marginAmount=1, quoteAmount=10000)
        print(tx_hash_openPosition.hex())
        # Wait for the transaction result to be confirmed
        w3.eth.waitForTransactionReceipt(tx_hash_openPosition)
        position_info = margin_test.getPosition(SETTING["WALLET_ADDRESS"])
        quote_amount = position_info[1]
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) >= 0.1:
            break
    print(">>>>>>>>>>>>>>>>Start to close the position>>>>>>>>>>>>>>>")
    for i in range(abs(int(quote_amount / (10000 * (10 ** 6))))):
        tx_hash_closePosition = margin_test.closePosition(trader=SETTING["WALLET_ADDRESS"], quoteAmount=10000)
        print(tx_hash_closePosition.hex())
        w3.eth.waitForTransactionReceipt(tx_hash_closePosition)
        margin_test.getPosition(SETTING["WALLET_ADDRESS"])
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) <= -0.1:
            break
    assert 1

def quick_increase():
    for i in range(10):
        tx_hash_openPosition = router_test.openPositionWeth(side=0, marginAmount=30, quoteAmount=500000)
        print(tx_hash_openPosition.hex())
        # Wait for the transaction result to be confirmed
        w3.eth.waitForTransactionReceipt(tx_hash_openPosition)
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        print("mark_price：", mark_price)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) >= 0.1:
            break
    position_info = margin_test.getPosition(SETTING["WALLET_ADDRESS"])
    margin_test.closePosition(trader=SETTING["WALLET_ADDRESS"],
                              quoteAmount=abs(int(position_info[1] / (10 ** 6))))


def quick_reduce():
    for i in range(10):
        tx_hash_openPosition = router_test.openPositionWeth(side=1, marginAmount=300, quoteAmount=500000)
        print(tx_hash_openPosition.hex())
        # Wait for the transaction result to be confirmed
        w3.eth.waitForTransactionReceipt(tx_hash_openPosition)
        mark_price = priceOracle_test.getMarkPrice(address=address)
        index_price = priceOracle_test.getIndexPrice(address=address)
        print("mark_price：", mark_price)
        # The market price fluctuates more than 10% , break
        if ((mark_price - index_price) / index_price) <= -0.1:
            break
    position_info = margin_test.getPosition(SETTING["WALLET_ADDRESS"])
    margin_test.closePosition(trader=SETTING["WALLET_ADDRESS"],
                              quoteAmount=abs(int(position_info[1] / (10 ** 6))))



if __name__ == '__main__':
    auto_trade_slow()