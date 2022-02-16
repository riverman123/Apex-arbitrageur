from brownie import  *
from config import config

SETTING = config.SETTING
CONTRACT_INFO = config.PRICEORACLE_CONTRACT_INFO
amm_address = config.AMM_CONTRACT_INFO["CONTRACT_ADDRESS"]
IPriceOracle = interface.IPriceOracle(CONTRACT_INFO["CONTRACT_ADDRESS"])



def getIndexPrice(address=amm_address):
    indexPrice = IPriceOracle.getIndexPrice(address)
    return indexPrice

def getMarkPrice(address=amm_address):
    markPrice = IPriceOracle.getMarkPrice(address)
    return markPrice/(10**18)


def getMarkPriceAcc(amm_address,  beta ,  quoteAmount  , negative  ):
    baseAmount = IPriceOracle.getMarkPriceAcc(amm_address,  beta ,  quoteAmount  , negative)
    return quoteAmount/baseAmount * 10**12


def main():
    t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    print(t.events)
    print("base_limit:", sys.maxsize)