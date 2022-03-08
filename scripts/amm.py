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
IAmm = interface.IAmm(CONTRACT_INFO["pairs"]["ETH/USD"]["amm"])


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
    #IAmm.rebase({"from": userA})
    # t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    # print(t.events)
    # reserve =  IAmm.getReserves()
    # print(reserve)
    # tx =  IAmm.rebaseFree({"from": userA})
    # print(tx.events)
    #print(rebaseFree())
    reserve =  IAmm.getReserves()
    secondsSinceEpoch = time.time()
    print(secondsSinceEpoch)