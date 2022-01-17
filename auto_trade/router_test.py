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

def openPositionWeth(side,marginAmount,quoteAmount,deadline=1957515898,baseToken=TOKEN_INFO["mockWETH"],quoteToken=TOKEN_INFO["mockUSDC"]):
    tx = contractObj.functions.openPositionWithWallet(baseToken,quoteToken,side,marginAmount*(10**18),quoteAmount*(10**6),marginAmount*(10**18),deadline).buildTransaction({
        'from': SETTING["WALLET_ADDRESS"],
        'gas': 1200000
    })
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx["nonce"] = nonce
    tx['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx, private_key=SETTING["WALLET_PRIVATE_KEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)

# tx_hash = openPositionWeth(0,1,10000)
# print(tx_hash.hex())
# w3.eth.waitForTransactionReceipt(tx_hash)
# print(getPosition(baseToken=TOKEN_INFO["mockWETH"],quoteToken=TOKEN_INFO["mockUSDC"],trader=SETTING["WALLET_ADDRESS"]))