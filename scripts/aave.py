from brownie import  *
from config import config

CONTRACT_INFO = config.CONTRACT_ADDRESS
ILendingPoolAddressesProvider = interface.ILendingPoolAddressesProvider(CONTRACT_INFO["mainnetLendingPoolAddressProvider"])
lendingPoolAddress = ILendingPoolAddressesProvider.getLendingPool()
ILendingPool = interface.ILendingPool(lendingPoolAddress)


# return userAccount data: totalCollateralETH,totalDebtETH,availableBorrowsETH,currentLiquidationThreshold,ltv,healthFactor
def getUserAccountData(userAccount):
    userAccountData = ILendingPool.getUserAccountData(userAccount)

    return userAccountData


def main():
    userAccountData = getUserAccountData("0x91fC7a8f9B21f020c0a9C6309c5437509142B063")
    print("healthFactor: ",userAccountData[5] / 10**18)

    
    