from brownie import  *
from brownie.convert import to_address
from config import config
import sys


# CONTRACT_INFO = config.CONTRACT_ADDRESS
# IRouter = interface.IRouter(CONTRACT_INFO["router"])


def getPosition(address, baseToken,quoteToken,trader):
    position_value = interface.IRouter(address).getPosition(baseToken,quoteToken,trader)
    return position_value

def openPositionRouter(address, side, marginAmount, quoteAmount,trader,deadline, baseToken, quoteToken):
    if side == 0:
        base_limit = 0
    else:
        base_limit = sys.maxsize*sys.maxsize
    # 将取到的地址，变得可用
    baseToken=to_address(baseToken)
    # buildTransaction
    tx = interface.IRouter(address).openPositionWithWallet(baseToken,quoteToken,side,int(marginAmount*(10**18)),int(quoteAmount*(10**6)),base_limit,deadline, {
        'from': trader})
    
    return tx


def closePosition(address , baseToken, quoteToken, quoteAmount,deadline, autoWithdraw, trader):
   
   
    # buildTransaction
    tx = interface.IRouter(address).closePosition(baseToken,quoteToken, quoteAmount,deadline,autoWithdraw, {
        'from': trader})
    
    return tx



def deposit(address , baseToken, quoteToken, amount,trader):
   
    tx0 = interface.IERC20(baseToken).approve(address,amount, {
        'from': trader});
   
    # buildTransaction
    tx = interface.IRouter(address).deposit(baseToken,quoteToken, trader, amount, {
        'from': trader})
    
    return tx



def closePositionETH(address , quoteToken, quoteAmount,deadline, trader):
   
    # buildTransaction
    tx = interface.IRouter(address).closePositionETH(quoteToken, quoteAmount,deadline, {
        'from': trader})
    
    return tx



def closePosition(address ,baseToken, quoteToken, quoteAmount,deadline, trader):
   
    # buildTransaction
    tx = interface.IRouter(address).closePosition(baseToken, quoteToken, quoteAmount,deadline, 0,{
        'from': trader})
    
    return tx




def openPositionETHWithWallet(address , side, marginAmount, quoteAmount,trader,deadline, quoteToken):
    if side == 0:
        base_limit = 0
    else:
        base_limit = sys.maxsize*sys.maxsize
    # 将取到的地址，变得可用
    # buildTransaction
    tx = interface.IRouter(address).openPositionETHWithWallet(quoteToken,side,quoteAmount,base_limit,deadline, {
        'from': trader,
        'value': marginAmount * 1e18})
    
    return tx


def openPositionWithMargin(address , side, marginAmount, quoteAmount,trader,deadline, quoteToken, baseToken):
    if side == 0:
        base_limit = 0
    else:
        base_limit = sys.maxsize*sys.maxsize
    # 将取到的地址，变得可用
    # buildTransaction
    tx = interface.IRouter(address).openPositionWithMargin(baseToken, quoteToken,side,quoteAmount,base_limit,deadline, {
        'from': trader})
    
    return tx    



def main():
    # t = chain.get_transaction('0xc8d5fee409163ea4cac15cff17a629576f87b10adb40e0c2ae70ef8504fe47a7')
    # print(t.events)
    print("base_limit:", sys.maxsize)
    # print(getPosition("0x4c3C90d25c93d08853b61c81cFd95d58c3B0C073", "", ""))


    
    
    

