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
    secondsSinceEpoch = time.time()
    print(secondsSinceEpoch)