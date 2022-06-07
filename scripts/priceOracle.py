from brownie import  *
from config import config

CONTRACT_INFO = config.CONTRACT_ADDRESS
IPriceOracle = interface.IPriceOracle('0x43Cbd3a59d6b02195836c38B47c5FCfA324E668d')



def getIndexPrice(address):
    indexPrice = IPriceOracle.getIndexPrice(address)
    return indexPrice

def getMarkPrice(address):
    markPrice = IPriceOracle.getMarkPrice(address)
    return markPrice/(10**18)


def getMarkPriceAcc(amm_address,  beta ,  quoteAmount  , negative  ):
    baseAmount = IPriceOracle.getMarkPriceAcc(amm_address,  beta ,  quoteAmount  , negative)
    return quoteAmount/baseAmount * 10**12


def main():
    # t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    # print(t.events)
    s = getMarkPriceAcc('0xa8cD3De0696Ef05eFd4f06492e14131c5A0A8aFF', 127, 2991470000, 1 )

    l= IPriceOracle.getMarkPriceInRatio('0xa8cD3De0696Ef05eFd4f06492e14131c5A0A8aFF',2991470000,0)
    print(s)
    print(l)
   