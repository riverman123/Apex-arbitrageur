from brownie import  *
from config import config
from helper import trade_helper
import os

SETTING = config.SETTING
CONTRACT_INFO = config.MARGIN_CONTRACT_INFO
IMargin = interface.IMargin(CONTRACT_INFO["CONTRACT_ADDRESS"])
PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key= PRIVATE_KEY_USER)
userRobert = accounts.add(private_key= PRIVATE_KEY_ROBOT )

# add margin to margin contract
def addMargin(trader, quoteAmount):
    tx = IMargin.addMargin(trader,quoteAmount*(10**6),{
        'from': trader,
        'gas': 1200000
    })

    return tx

# use margin removeMargin function to return traders margin
def removeMargin(trader,withdrawAmount):
    tx = IMargin.removeMargin(trader,trader,withdrawAmount,{
        'from': trader,
        'gas': 1200000
    })

    return tx

# use margin openPosition function to open position
def openPosition(trader,quoteAmount,side):
    tx = IMargin.OpenPosition(trader,side,quoteAmount*(10**6),{
        'from': trader,
        'gas': 1200000
    })
    return tx

# use margin closePosition function to close position
# todo robot 
def closePosition(trader,quoteAmount):
    tx = IMargin.closePosition(trader,quoteAmount,{
        'from': trader,
        'gas': 1200000
    })
    return tx

# use margin getPosition function to get position information
def getPosition(trader):
    position_value = IMargin.getPosition(trader)
    position0 = position_value[0]/(10**18)
    position1 = position_value[1]/(10**6)
    position2 = position_value[2]/(10**18)
    return position_value

def getPositionAccurate(trader):
    position_value = IMargin.getPosition(trader)
    return position_value

# use margin getWithdrawable function to get position maximum withdraw margin value
def getWithdrawable(trader):
    user_wthdrawAble = IMargin.getWithdrawable(trader)
    return user_wthdrawAble

def calFundingFee(trader):
    funding_value = IMargin.calFundingFee(trader)
    funding_value = funding_value/(10**18)
    return funding_value

def calFundingFeeRaw(trader):
    funding_value = IMargin.calFundingFee(trader)
    return funding_value


def getDebtRatio(trader):
    debt_Ratio = IMargin.calDebtRatio(trader)
    print(debt_Ratio)
    return debt_Ratio

def toliquidate(trader):
    tx = IMargin.liquidate(trader,{
        'from': trader,
        'gas': 1200000
    })
    return tx

def return_margin(trader):
    user_wthdrawAble = getWithdrawable(trader)
    if user_wthdrawAble > 0 :
        removeMargin(trader=trader,withdrawAmount=user_wthdrawAble)

def main():
    trader = SETTING["ADDRESS_USER"]
    position = getPosition(SETTING["ADDRESS_USER"])
    print("user: ",position)
    position = getPosition(SETTING["ADDRESS_ROBOT"])
    print("user: ",position)
    tx=  closePosition(SETTING["ADDRESS_USER"], abs(position[1]))
    print(tx)
    amount = getWithdrawable(SETTING["ADDRESS_USER"]) 
    removeMargin(trader,amount)
    
    