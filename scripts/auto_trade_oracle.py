from brownie import *
import os
import json
from scripts import  amm, margin, router
from config import config
from dotenv import load_dotenv
import time
import random
import requests, json 
load_dotenv()


url = "https://raw.githubusercontent.com/ApeX-Protocol/config/main/contracts-test.json"
priceurl = "https://api.etherscan.io/api?module=stats&action=ethprice&apikey=2QJHBURFK52GJSFSNHCJA37P6I9JC14YPK"
                
perp_pair = "ETH-USD-SWAP"
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userRobert = accounts.add(private_key = PRIVATE_KEY_ROBOT)
deadline = 1948807072;

marginAmount= 0.05
sleep = 120

def fetchContractAddress():
      response = requests.get(url)
      data = response.json()
      #print(data)
      routerAddress = data["router"]["address"]
      ammAddress = data["pairs"]["ETH/USD"]["amm"]
      marginAddress = data["pairs"]["ETH/USD"]["margin"]
      return [routerAddress,ammAddress,marginAddress ]

def fetchEthPrice():
      response = requests.get(priceurl)
      data = response.json()
      #print(data)
      
      return  data["result"]["ethusd"]


def auto_trade():
    count = 0
    routerAddress = "0x9C240130a08CEf0bc8903ccBE2EEcc731Cb7aAe5"
    ammAddress = "0x01A3eae4edD0512d7d1e3B57eCD40A1A1b1076EE"
    marginAddress = "0xb6815C460ED87353Af9D7e84B46659A99aB2D6F6"
    try:
        baseToken  = interface.IAmm(ammAddress).baseToken()
        quoteToken = interface.IAmm(ammAddress).quoteToken()
    except  Exception as err:
            print("query token address wrong!");      
            print(err);         
 
    while True:    
      try:
            quoteAmount = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
            baseSize = margin.getPositionAccurate(marginAddress ,userRobert.address)[0]
           # print("quoteAmount",quoteAmount);
            print("baseSize", baseSize)

            if(baseSize< 50 * 10**18 ):
                print("deposit margin")
                router.deposit(routerAddress, baseToken, quoteToken,  200 * 10**18 ,userRobert.address )
            
            if(quoteAmount>200000000000):
                # 2W close position
                print("close big position wrong")
                router.closePosition(routerAddress,baseToken, quoteToken , quoteAmount=abs(quoteAmount), deadline = deadline, trader = userRobert.address)
               

            #  # withdraw margin
            #  withdrawableAmount = margin.getWithdrawable(marginAddress, userRobert.address);
            #  router.withdrawETH(routerAddress,quotetoken ,  withdrawableAmount)
            
            # 配置开仓量 
            isLong = random.randint(0,1)
            quoteAmountRandom = random.randint(1000,50000) * 1000000
            reserves = interface.IAmm(ammAddress).getReserves()
            pricedex = reserves[1]* 10**12/reserves[0]
            priceCex = fetchEthPrice()
            # print("pricedex:", pricedex)
            # print("pricecex:", priceCex)
            spread = (pricedex - float(priceCex))/float(priceCex)
            if(spread> 0.02 ):
                isLong = 0  

    
            if(spread < -0.02):
                isLong = 1
            #print("spread", spread)    
            try:
                if(isLong): 
                    print("open long")
                    router.openPositionWithMargin(routerAddress,0, marginAmount, quoteAmountRandom,userRobert.address, deadline, quoteToken, baseToken );
                    

                else:
                    print("open short")
                    router.openPositionWithMargin(routerAddress,1, marginAmount, quoteAmountRandom,userRobert.address, deadline, quoteToken, baseToken );
                    
            except  Exception as err:
                print("open position wrong!");      
                print(err);      
            
            count+=1
            print("count", count)

            time.sleep(sleep)  
            if(count %5 == 0) :
                
                quoteAmount1 = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
                try:
                    router.closePosition(routerAddress, baseToken, quoteToken , quoteAmount=abs(quoteAmount1), deadline = deadline, trader = userRobert.address)
                except  Exception as err:
                    print("close position wrong!");  
                    print(err);
                count =0
                [routerAddress,ammAddress, marginAddress ]=fetchContractAddress();
                
                baseToken  = interface.IAmm(ammAddress).baseToken()
                quoteToken = interface.IAmm(ammAddress).quoteToken()

                


                time.sleep(sleep)  
      except  Exception as err:
            print(err);   
        
        
    
    


def main():
      
        try: 
            auto_trade();
            
        except  Exception as err:
            print(err);
       
        finally:
            print('finally')
            time.sleep(sleep)  
 
            auto_trade()

