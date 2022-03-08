from brownie import  *
from config import config
import os


PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key= PRIVATE_KEY_USER)
userRobert = accounts.add(private_key= PRIVATE_KEY_ROBOT )

# add margin to margin contract
def addMargin(address , trader, quoteAmount):
    tx = interface.IMargin(address).addMargin(trader,quoteAmount*(10**6),{
        'from': trader,
        'gas': 1200000
    })

    return tx

# use margin removeMargin function to return traders margin
def removeMargin(address,trader,withdrawAmount):
    tx = interface.IMargin(address).removeMargin(trader,trader,withdrawAmount,{
        'from': trader,
        'gas': 1200000
    })

    return tx

# use margin openPosition function to open position
def openPosition(address,trader,quoteAmount,side):
    tx = interface.IMargin(address).openPosition(trader,side,quoteAmount,{
        'from': trader,
        'gas': 1200000
    })
    return tx

# use margin closePosition function to close position
# todo robot 
def closePosition(address,trader,quoteAmount):
    tx = interface.IMargin(address).closePosition(trader,quoteAmount,{
        'from': trader
    })
    return tx

# use margin getPosition function to get position information
def getPositionAccurate(address,trader):
    position_value = interface.IMargin(address).getPosition(trader)
    return position_value

# use margin getWithdrawable function to get position maximum withdraw margin value
def getWithdrawable(address,trader):
    user_wthdrawAble = interface.IMargin(address).getWithdrawable(trader)
    return user_wthdrawAble

def calFundingFee(address,trader):
    funding_value = interface.IMargin(address).calFundingFee(trader)
    #funding_value = funding_value/(10**18)
    return funding_value

def getDebtRatio(address,trader):
    debt_Ratio = interface.IMargin(address).calDebtRatio(trader)
    print(debt_Ratio)
    return debt_Ratio

def toliquidate(address,trader):
    tx = interface.IMargin(address).liquidate(trader,{
        'from': trader
    })
    return tx

def return_margin(address,trader):
    user_wthdrawAble = getWithdrawable(trader)
    if user_wthdrawAble > 0 :
        removeMargin(trader=trader,withdrawAmount=user_wthdrawAble)

def main():
    
    position = getPosition(userA.address)
    print("user: ",position)
    # position = getPosition(SETTING["ADDRESS_ROBOT"])
    # print("user: ",position)
    # tx=  closePosition(SETTING["ADDRESS_USER"], abs(position[1]))
    # print(tx)
    # amount = getWithdrawable(SETTING["ADDRESS_USER"]) 
    # removeMargin(trader,amount)
    
    