from brownie import  *
from config import config


SETTING = config.SETTING
CONTRACT_INFO = config.CONFIG_INFO
Iconfig = interface.IAmm(CONTRACT_INFO["CONTRACT_ADDRESS"])



def getBeta():
    beta = Iconfig.beta()
    return beta/100