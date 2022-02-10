from brownie import  *
from brownie.convert import to_address
from config import config
import sys


CONTRACT_INFO = config.ROUTER_CONTRACT_INFO
TOKEN_INFO = config.TOKEN_INFO
IRouter = interface.IRouter(CONTRACT_INFO["CONTRACT_ADDRESS"])


def getPosition(baseToken,quoteToken,trader):
    position_value = IRouter.getPosition(baseToken,quoteToken,trader)
    return position_value

def openPositionRouter(side, marginAmount, quoteAmount,trader,deadline=1957515898, baseToken=TOKEN_INFO["BBB"], quoteToken=TOKEN_INFO["mockUSDC"]):
    if side == 0:
        base_limit = 0
    else:
        base_limit = sys.maxsize*sys.maxsize
    # 将取到的地址，变得可用
    baseToken=to_address(baseToken)
    # buildTransaction
    tx = IRouter.openPositionWithWallet(baseToken,quoteToken,side,int(marginAmount*(10**18)),int(quoteAmount*(10**6)),base_limit,deadline, {
        'from': trader,
        'gas': 1200000})
    
    return tx

def main():
    t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    print(t.events)
    print("base_limit:", sys.maxsize)
    # print(getPosition("0x4c3C90d25c93d08853b61c81cFd95d58c3B0C073", "", ""))
    
    

