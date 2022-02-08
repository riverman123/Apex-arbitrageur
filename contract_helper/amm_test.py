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

def getReservesAccurate():
    reserves = contractObj.functions.getReserves().call()
    return reserves

def setBaseReserve(base_reserve):
    print("base_reserve:",base_reserve)
    tx_dic = contractObj.functions.setBaseReserve(base_reserve).buildTransaction({
        'from': SETTING["ADDRESS_USER"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx_dic=tx_dic,trader=SETTING["ADDRESS_USER"],trader_key=SETTING["PRIVATE_KEY_USER"])
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

def rebaseFree():
    tx_dic = contractObj.functions.setBaseReserve().buildTransaction({
        'from': SETTING["ADDRESS_USER"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx_dic=tx_dic,trader=SETTING["ADDRESS_USER"],trader_key=SETTING["PRIVATE_KEY_USER"])
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

if __name__ == '__main__':
    setBaseReserve(28144364328489465569859)

