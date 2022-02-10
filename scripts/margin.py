from brownie import  *
from config import config
from helper import trade_helper

SETTING = config.SETTING
CONTRACT_INFO = config.MARGIN_CONTRACT_INFO
IMargin = interface.IMargin(CONTRACT_INFO["CONTRACT_ADDRESS"])

# add margin to margin contract
def addMargin(trader,trader_key, quoteAmount):
    tx_dic = IMargin.addMargin(trader,quoteAmount*(10**6),{
        'from': trader,
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx_dic=tx_dic,trader=trader,trader_key=trader_key)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin removeMargin function to return traders margin
def removeMargin(trader,trader_key,withdrawAmount):
    tx_dic = IMargin.removeMargin(trader,trader,withdrawAmount,{
        'from': trader,
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx_dic=tx_dic,trader=trader,trader_key=trader_key)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin openPosition function to open position
def openPosition(trader,quoteAmount,side):
    tx = IMargin.OpenPosition(trader,side,quoteAmount*(10**6),{
        'from': SETTING["ADDRESS_ROBOT"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin closePosition function to close position
def closePosition(trader,trader_key,quoteAmount):
    tx = IMargin.closePosition(trader,quoteAmount,{
        'from': SETTING["ADDRESS_ROBOT"],
        'gas': 1200000
    })
    tx_hash = trade_helper.sendTransation(tx,trader=trader,trader_key=trader_key)
    w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash

# use margin getPosition function to get position information
def getPosition(trader):
    position_value = IMargin.getPosition(trader)
    position_value[0] = position_value[0]/(10**18)
    position_value[1] = position_value[1]/(10**6)
    position_value[2] = position_value[2]/(10**18)
    return position_value

def getPositionAccurate(trader):
    position_value = IMargin.getPosition(trader)
    return position_value

# use margin getWithdrawable function to get position maximum withdraw margin value
def getWithdrawable(trader):
    user_wthdrawAble = IMargin.getWithdrawable(trader)
    return user_wthdrawAble

def getFunding(trader):
    funding_value = IMargin.calFundingFee(trader)
    funding_value = funding_value/(10**18)
    return funding_value

def getFundingAccurate(trader):
    funding_value = IMargin.calFundingFee(trader)
    return funding_value


def getDebtRatio(trader):
    debt_Ratio = IMargin.calDebtRatio(trader)
    print(debt_Ratio)
    return debt_Ratio

def toliquidate(trader,trader_key):
    tx = IMargin.liquidate(trader,{
        'from': trader,
        'gas': 1200000
    })
    return tx


def main():
    t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    print(t.events)
    print(getDebtRatio("0x4c3C90d25c93d08853b61c81cFd95d58c3B0C073"))
    