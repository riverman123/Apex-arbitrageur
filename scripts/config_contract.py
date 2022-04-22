from brownie import  *
import os
from dotenv import load_dotenv
load_dotenv()

PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userA = accounts.add(private_key= PRIVATE_KEY_USER)
userRobert = accounts.add(private_key= PRIVATE_KEY_ROBOT )
print(userA.address)

# CONTRACT_INFO = config.CONTRACT_ADDRESS
# Iconfig = interface.IConfig(CONTRACT_INFO["config"])



def getBeta():
    beta = Iconfig.beta()
    return beta/100

def setBeta(beta):
    hash_tx = Iconfig.setBeta(beta, {'from': userA})
    return hash_tx

def getBetaRaw():
    beta = Iconfig.beta()
    return beta

def main():
    # t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    # print(t.events)
    # print(getBeta())
    # print(Iconfig.tradingSlippage())
    print(userA.address)


