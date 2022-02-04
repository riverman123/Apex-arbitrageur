from web3.main import Web3
from config import config
from helper import trade_helper

SETTING = config.SETTING
CONTRACT_INFO = config.AMM_CONTRACT_INFO
w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])

def getReserves(is_print=False):
    reserves = contractObj.functions.getReserves().call()
    if is_print == True:
        print('x:',reserves[0]/(10**18))
        print('y:',reserves[1]/(10**6))
    return reserves

if __name__ == '__main__':
    getReserves()

