from brownie import  *
from config import config
import requests
import json
import pandas as pd

CONTRACT_INFO = config.CONTRACT_ADDRESS
networkname = network.show_active()
lendingPoolProviderAddress = CONTRACT_INFO["LendingPoolAddressProvider"][networkname]
ILendingPoolAddressesProvider = interface.ILendingPoolAddressesProvider(lendingPoolProviderAddress)
lendingPoolAddress = ILendingPoolAddressesProvider.getLendingPool()
ILendingPool = interface.ILendingPool(lendingPoolAddress)
aaveOacleAddress = interface.IAAVEPriceOracle(ILendingPoolAddressesProvider.getPriceOracle())
querySql = """query($id: String!) {
            users (where: {id: $id}) {
                borrowHistory (orderBy: timestamp) { 
                    amount 
                    reserve{
                        symbol
                        decimals
                        underlyingAsset
                        vToken{
                            id
                        }
                    }
                    userReserve{
                        currentTotalDebt
                    }
                    
                }
    
                repayHistory (orderBy: timestamp){ 
                    amount 
                    reserve{
                        symbol
                        decimals
                    }
                }
            }
        }"""
url = 'https://api.thegraph.com/subgraphs/name/aave/protocol-v2'

# return userAccount data: totalCollateralETH,totalDebtETH,availableBorrowsETH,currentLiquidationThreshold,ltv,healthFactor
def getUserAccountData(userAccount):
    userAccountData = ILendingPool.getUserAccountData(userAccount)

    return userAccountData

    # price return in ETH
def getPrice(asset):
    priceInETH = aaveOacleAddress.getAssetPrice(asset)
    return priceInETH

def getInterest(userAddress,URL=url):
    variables = {'id': userAddress}
    r = requests.post(URL, json={'query': querySql,'variables': variables})
    json_data = json.loads(r.text)
    df_borrow_data = json_data['data']['users'][0]['borrowHistory']
    df_repay_data = json_data['data']['users'][0]['repayHistory']

    total_borrow = {}
    # amount need to be summed by loop in case of overflow : https://github.com/pandas-dev/pandas/issues/18842
    for borrowRecord in df_borrow_data:
        symbol = borrowRecord["reserve"]["symbol"]
        decimals = int(borrowRecord["reserve"]["decimals"])
        vToken = borrowRecord["reserve"]["vToken"]["id"]
        currentTotalDebt = borrowRecord["userReserve"]["currentTotalDebt"]

        if symbol not in total_borrow:
            total_borrow[symbol] = {"amount": 0}

        if "decimals" not in total_borrow[symbol]:
            total_borrow[symbol]["decimals"] = decimals

        if "vToken" not in total_borrow[symbol]:
            total_borrow[symbol]["vToken"] = vToken
        
        if "currentTotalDebt" not in total_borrow[symbol]:
            total_borrow[symbol]["currentTotalDebt"] = int(currentTotalDebt)

        total_borrow[symbol]["amount"] += int(borrowRecord['amount'])

    total_repay = {}
    for repayRecord in df_repay_data:
        symbol = repayRecord["reserve"]["symbol"]
        
        if symbol not in total_repay:
            total_repay[symbol] = {"amount": 0}

        total_repay[symbol]["amount"] += int(repayRecord['amount'])

    tota_interest = {}
    for symbol in total_repay.keys():
        currentDebt = 0
        if total_borrow[symbol]["currentTotalDebt"] != 0:
            currentDebt = getCurrentDebt(total_borrow[symbol]["vToken"],userAddress)

        tota_interest[symbol] = (total_repay[symbol]["amount"] + currentDebt - total_borrow[symbol]["amount"]) / 10**total_borrow[symbol]["decimals"]

    return tota_interest

def getCurrentDebt(debtTokenAddress,userAddress):
    variableDebtToken = interface.IVariableDebtToken(debtTokenAddress)
    return variableDebtToken.balanceOf(userAddress)


def main():
    userAddress = "0xFE63eDdC467E3E7bB6804ab21eAA18289355d02b".lower()
    matic_url = "https://api.thegraph.com/subgraphs/name/aave/aave-v2-matic"
    interest = getInterest(userAddress,URL=matic_url)
    print(interest)
    
