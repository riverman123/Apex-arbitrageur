from brownie import  *
import os
import time
from config import config

from dotenv import load_dotenv
load_dotenv()

PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key= PRIVATE_KEY_USER)
userRobert = accounts.add(private_key= PRIVATE_KEY_ROBOT )

CONTRACT_INFO = config.CONTRACT_ADDRESS

def getReserves(address):
    reserves = interface.IAmm(address).getReserves()
    return reserves

def  getBaseToken(address) : 
     baseToken = interface.IAmm(address).baseToken()
     return baseToken

def  getQuoteToken(address) : 
     quoteToken = interface.IAmm(address).quoteToken()
     return quoteToken


def main():
    address = "0xa8cD3De0696Ef05eFd4f06492e14131c5A0A8aFF"
    reserves = getReserves(address)
    print(reserves[0])
    print(reserves[1])
    print(interface.IAmm(address).getFeeLiquidity())
    print(interface.IAmm(address).getTheMaxBurnLiquidity())
    print(interface.IERC20(address).totalSupply())
    print(interface.IAmm(address).getRealBaseReserve());

    #9.78372558 btc
    #511054.208734 usdc

    # netpositon -11063.62usdc
    #fee liquidity 218062
    #maxLiquidity 17140253131
    #total Liquidity 22360469331
    #realBaseReserve 10.00503189