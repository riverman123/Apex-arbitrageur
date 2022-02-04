from web3.main import Web3
from config import config

SETTING = config.SETTING
CONTRACT_INFO = config.MARGIN_CONTRACT_INFO

w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])

def sendTransation(tx_dic,trader,trader_key):
    nonce = w3.eth.getTransactionCount(trader)
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=trader_key)

    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)

def sendTransationWithMoreGas(tx_dic, gwei,trader,trader_key):
    nonce = w3.eth.getTransactionCount(trader)
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=trader_key)
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)

def getTransationInfo(tx_hash):
    result = w3.eth.getTransactionReceipt(tx_hash)
    if result["status"] != 1:
        returnData = result["returnData"][10:]
        print("returnData",Web3.toText(returnData))


if __name__ == '__main__':
    getTransationInfo("0x10daf6780cfca57fd006b522b8a478ce02e9fc11f9ebada8b95e2ce22f24ae76")