from web3.main import Web3
from config import config
from helper import trade_helper
import sys

SETTING = config.SETTING
CONTRACT_INFO = config.ROUTER_CONTRACT_INFO
TOKEN_INFO = config.TOKEN_INFO

w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])


def getPosition(baseToken,quoteToken,trader):
    position_value = contractObj.functions.getPosition(baseToken,quoteToken,trader).call()
    return position_value

def openPositionRouter(side, marginAmount, quoteAmount,trader,trader_key,deadline=1957515898, baseToken=TOKEN_INFO["BBB"], quoteToken=TOKEN_INFO["mockUSDC"]):
    if side == 0:
        base_limit = 0
    else:
        base_limit = sys.maxsize*sys.maxsize
    # 将取到的地址，变得可用
    baseToken=Web3.toChecksumAddress(baseToken)
    # buildTransaction
    tx_dic = contractObj.functions.openPositionWithWallet(baseToken,quoteToken,side,int(marginAmount*(10**18)),int(quoteAmount*(10**6)),base_limit,deadline).buildTransaction({
        'from': trader,
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx_dic=tx_dic,trader=trader,trader_key=trader_key)
    w3.eth.waitForTransactionReceipt(tx_hash)
    result = w3.eth.getTransactionReceipt(tx_hash)
    if result["status"] != 1:
        returnData = result["returnData"][10:]
        print("returnData",Web3.toText(returnData))
    return tx_hash

# tx_hash = openPositionWeth(0,1,10000)
# print(tx_hash.hex())
# w3.eth.waitForTransactionReceipt(tx_hash)

if __name__ == '__main__':
    print("base_limit:", sys.maxsize)

