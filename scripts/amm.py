from brownie import  *
import os
from config import config

from dotenv import load_dotenv
load_dotenv()

PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key= PRIVATE_KEY_USER)
userRobert = accounts.add(private_key= PRIVATE_KEY_ROBOT )

CONTRACT_INFO = config.AMM_CONTRACT_INFO
#IAmm = interface.IAmm(CONTRACT_INFO["CONTRACT_ADDRESS"])
IAmm = interface.IAmm('0x59b7fefdae5000ef5528317a381bcbe4b6a26758')


def getReserves(is_print=False):
    reserves = IAmm.getReserves()
    if is_print == True:
        print('x:',reserves[0]/(10**18))
        print('y:',reserves[1]/(10**6))
    return reserves

def getReservesAccurate():
    reserves = IAmm.getReserves()
    return reserves

def setBaseReserve(base_reserve):
    print("base_reserve:",base_reserve)
    tx = IAmm.setBaseReserve(base_reserve , {'from': userA})
    return tx

def rebaseFree():
    tx = IAmm.rebaseFree({'from': userA})
    return tx

def main():
    IAmm.rebase({"from": userA})
    # t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    # print(t.events)
    # reserve =  IAmm.getReserves()
    # print(reserve)
    # tx =  IAmm.rebaseFree({"from": userA})
    # print(tx.events)
    print(rebaseFree())
    # reserve =  IAmm.getReserves()
    # print(reserve)