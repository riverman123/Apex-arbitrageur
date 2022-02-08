from web3.main import Web3
from config import config

SETTING = config.SETTING
CONTRACT_INFO = config.PRICEORACLE_CONTRACT_INFO

w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])

def getIndexPrice(address):
    indexPrice = contractObj.functions.getIndexPrice(address).call()
    return indexPrice

def getMarkPrice(address):
    markPrice = contractObj.functions.getMarkPrice(address).call()
    return markPrice
