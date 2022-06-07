import ccxt
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



def auto_trade():
    count = 0
    routerAddress = "0x9C240130a08CEf0bc8903ccBE2EEcc731Cb7aAe5"
    ammAddress = "0x01A3eae4edD0512d7d1e3B57eCD40A1A1b1076EE"
    marginAddress = "0xb6815C460ED87353Af9D7e84B46659A99aB2D6F6"
    
    baseToken  = interface.IAmm(ammAddress).baseToken()
    quoteToken = interface.IAmm(ammAddress).quoteToken()
 
    while True:    
  
         quoteAmount = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
         print("quoteAmount",quoteAmount);
         
         if(quoteAmount>10000000000):
               # 2W close position
            router.closePositionETH(routerAddress, quoteToken , quoteAmount=abs(quoteAmount), deadline = deadline, trader = userRobert.address)
            print("close big position wrong")

        #  # withdraw margin
        #  withdrawableAmount = margin.getWithdrawable(marginAddress, userRobert.address);
        #  router.withdrawETH(routerAddress,quotetoken ,  withdrawableAmount)
        
        
         isLong = random.randint(0,1)
         quoteAmountRandom = random.randint(50,1000) * 1000000
        
         try:
          if(isLong): 
            
              router.openPositionETHWithWallet(routerAddress,0, marginAmount, quoteAmountRandom,userRobert.address, deadline, quoteToken );
              print("open long")

          else:

              router.openPositionETHWithWallet(routerAddress,1, marginAmount, quoteAmountRandom,userRobert.address, deadline, quoteToken );
              print("open short")
         except  Exception as err:
              print("open position wrong!");      
              print(err);      
         
         count+=1
         print("count", count)

         time.sleep(sleep)  
         if(count %5 == 0) :
              
               quoteAmount1 = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
               try:
                 router.closePositionETH(routerAddress, quoteToken , quoteAmount=abs(quoteAmount1), deadline = deadline, trader = userRobert.address)
               except  Exception as err:
                 print("close position wrong!");  
                 print(err);
               count =0
               [routerAddress,ammAddress, marginAddress ]=fetchContractAddress();
              #  print("routerAddress", routerAddress)
              #  print("ammAddress", ammAddress)
              #  print("marginAddress", marginAddress)
               
               baseToken  = interface.IAmm(ammAddress).baseToken()
               quoteToken = interface.IAmm(ammAddress).quoteToken()
               time.sleep(sleep)  
 
        
        
    
    


def main():
      
        try: 
            auto_trade();
            
        except  Exception as err:
            print(err);
       
        finally:
            print('finally')
            time.sleep(sleep)  
 
            auto_trade()

