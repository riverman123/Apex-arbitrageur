from web3.main import Web3
from config import config

SETTING = config.SETTING
CONTRACT_INFO = config.MARGIN_CONTRACT_INFO

w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])

def sendTransation(tx_dic,trader=SETTING["ADDRESS_ROBOT"],trader_key=SETTING["PRIVATE_KEY_ROBOT"]):
    nonce = w3.eth.getTransactionCount(trader)
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=trader_key)
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)

def sendTransationWithMoreGas(tx_dic, gwei,trader=SETTING["ADDRESS_ROBOT"],trader_key=SETTING["PRIVATE_KEY_ROBOT"]):
    nonce = w3.eth.getTransactionCount(trader)
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=trader_key)
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)

