from brownie import  *
from config import config


SETTING = config.SETTING
CONTRACT_INFO = config.CONFIG_INFO
Iconfig = interface.IConfig(CONTRACT_INFO["CONTRACT_ADDRESS"])



def getBeta():
    beta = Iconfig.beta()
    return beta/100

def main():
    # t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    # print(t.events)
    print(getBeta())
    print(Iconfig.tradingSlippage())
