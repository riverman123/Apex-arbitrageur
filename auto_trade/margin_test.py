from web3.main import Web3
from config import config
from helper import trade_helper

SETTING = config.SETTING
CONTRACT_INFO = config.MARGIN_CONTRACT_INFO
w3 = Web3(Web3.HTTPProvider(SETTING["URL"]))
contractObj = w3.eth.contract(address=CONTRACT_INFO["CONTRACT_ADDRESS"], abi=CONTRACT_INFO["CONTRACT_ABI"])

# add margin to margin contract
def addMargin(trader, quoteAmount):
    tx = contractObj.functions.addMargin(trader,quoteAmount*(10**6)).buildTransaction({
        'from': trader,
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin removeMargin function to return traders margin
def removeMargin(trader,withdrawAmount):
    tx = contractObj.functions.removeMargin(trader,trader,withdrawAmount).buildTransaction({
        'from': SETTING["ADDRESS_ROBOT"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin openPosition function to open position
def openPosition(trader,quoteAmount,side):
    tx = contractObj.functions.OpenPosition(trader,side,quoteAmount*(10**6)).buildTransaction({
        'from': SETTING["ADDRESS_ROBOT"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin closePosition function to close position
def closePosition(trader,trader_key,quoteAmount):
    tx = contractObj.functions.closePosition(trader,quoteAmount).buildTransaction({
        'from': SETTING["ADDRESS_ROBOT"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx,trader=trader,trader_key=trader_key)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin getPosition function to get position information
def getPosition(trader):
    position_value = contractObj.functions.getPosition(trader).call()
    position_value[0] = position_value[0]/(10**18)
    position_value[1] = position_value[1]/(10**6)
    position_value[2] = position_value[2]/(10**18)
    print(position_value)
    return position_value

def getPositionAccurate(trader):
    position_value = contractObj.functions.getPosition(trader).call()
    return position_value

# use margin getWithdrawable function to get position maximum withdraw margin value
def getWithdrawable(trader):
    user_wthdrawAble = contractObj.functions.getWithdrawable(trader).call()
    print(user_wthdrawAble)
    return user_wthdrawAble

def getFunding(trader):
    funding_value = contractObj.functions.calFundingFee(trader).call()
    funding_value = funding_value/(10**18)
    return funding_value

def getDebtRatio(trader):
    debt_Ratio = contractObj.functions.calDebtRatio(trader).call()
    print(debt_Ratio)
    return debt_Ratio

def toliquidate(trader,trader_key):
    tx = contractObj.functions.liquidate(trader).buildTransaction({
        'from': trader,
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx,trader=trader,trader_key=trader_key)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash