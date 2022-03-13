from typing_extensions import Self
import requests
import json
import pandas as pd
from sqlalchemy import BIGINT

class AAVE_GRAPH:
    def __init__(self):
        self.querySql = """query($id: String!) {
            users (where: {id: $id}) {
                borrowHistory (orderBy: timestamp) { 
                    amount 
                    borrowRate
                    timestamp
                    variableTokenDebt
                }
    
                repayHistory (orderBy: timestamp){ 
                    amount 
                    timestamp
                }
            }
        }"""
        self.url = 'https://api.thegraph.com/subgraphs/name/aave/protocol-v2'
        
    def set_url(self,URL):
        self.url = URL

    def get_interest(self,userAddress):
        variables = {'id': userAddress}
        r = requests.post(self.url, json={'query': self.querySql,'variables': variables})
        json_data = json.loads(r.text)
        print(json_data)
        df_borrow_data = pd.DataFrame(json_data['data']['users'][0]['borrowHistory'])
        df_repay_data = pd.DataFrame(json_data['data']['users'][0]['repayHistory'])
        # total_borrow = df_borrow_data['amount'].sum()
        # total_repay = df_repay_data['amount'].sum()
        # sum amount by loop in case of overflow : https://github.com/pandas-dev/pandas/issues/18842
        total_borrow = 0
        for amout in df_borrow_data['amount']:
            total_borrow += int(amout)
        print(total_borrow)
        total_repay = 0
        for amout in df_repay_data['amount']:
            total_repay += int(amout)
        print(total_repay)
        return total_repay - total_borrow

if __name__ == "__main__":
    aaveGraph = AAVE_GRAPH()
    interest = aaveGraph.get_interest("0x91fc7a8f9b21f020c0a9c6309c5437509142b063")
    print(interest)