from web3.main import Web3
from config import config

SETTING = config.SETTING
CONTRACT_INFO = config.ROUTER_CONTRACT_INFO
TOKEN_INFO = config.TOKEN_INFO

w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])


def getPosition(baseToken,quoteToken,trader):
    position_value = contractObj.functions.getPosition(baseToken,quoteToken,trader).call()
    return position_value

def openPositionRouter(side, marginAmount, quoteAmount, deadline=1957515898, baseToken=TOKEN_INFO["BBB"], quoteToken=TOKEN_INFO["mockUSDC"]):
    # 将取到的地址，变得可用
    baseToken=Web3.toChecksumAddress(baseToken)
    # buildTransaction
    tx = contractObj.functions.openPositionWithWallet(baseToken,quoteToken,side,marginAmount*(10**18),quoteAmount*(10**6),marginAmount*(10**18*100),deadline).buildTransaction({
        'from': SETTING["ADDRESS_ROBOT"],
        'gas': 1200000
    })
    nonce = w3.eth.getTransactionCount(SETTING["ADDRESS_ROBOT"])
    tx["nonce"] = nonce
    tx['gasPrice'] = w3.eth.gasPrice
    # 签名确认交易
    sign_tx = w3.eth.account.signTransaction(tx, private_key=SETTING["PRIVATE_KEY_ROBOT"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)

# tx_hash = openPositionWeth(0,1,10000)
# print(tx_hash.hex())
# w3.eth.waitForTransactionReceipt(tx_hash)
