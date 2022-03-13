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

    # amount need to be summed by loop in case of overflow : https://github.com/pandas-dev/pandas/issues/18842
    total_borrow = 0
    for borrowRecord in df_borrow_data:
        total_borrow += int(borrowRecord['amount'])

    total_repay = 0
    for repayRecord in df_repay_data:
        total_repay += int(repayRecord['amount'])

    vTokenAddress = df_borrow_data[0]['reserve']['vToken']['id']
    currentDebt = getCurrentDebt(vTokenAddress,userAddress)
    totalInterest = (total_repay + currentDebt - total_borrow) / 10 ** int(df_borrow_data[0]['reserve']['decimals'])
    interestList = {"symbol": df_borrow_data[0]['reserve']['symbol'], "Total Interest": totalInterest }

    return interestList

def getCurrentDebt(debtTokenAddress,userAddress):
    variableDebtToken = interface.IVariableDebtToken(debtTokenAddress)
    return variableDebtToken.balanceOf(userAddress)


def main():
    userAddress = "0xFE63eDdC467E3E7bB6804ab21eAA18289355d02b".lower()
    matic_url = "https://api.thegraph.com/subgraphs/name/aave/aave-v2-matic"
    interest = getInterest(userAddress,URL=matic_url)
    print(interest)
