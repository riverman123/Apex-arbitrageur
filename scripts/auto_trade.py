import ccxt
from brownie import *
import os
import json
from scripts import  amm, margin, router
from config import config
from dotenv import load_dotenv
import time
import random
load_dotenv()

ammAddress = "0x9Da2964847B82C7DBB13C36AeE0E80E530754edc"
marginAddress = "0xA91BfB9F505b9eB4CC44944F1D8a3DcBF3CB8eac"
routerAddress = "0x70b91fc6a35c62aa6f14a62d09a84797f1e4346b"

baseToken  = interface.IAmm(ammAddress).baseToken()
quoteToken = interface.IAmm(ammAddress).quoteToken()
perp_pair = "ETH-USD-SWAP"
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userRobert = accounts.add(private_key=PRIVATE_KEY_ROBOT)
deadline = 1948807072;

marginAmount= 0.05




def auto_trade():
    count = 0
    while True:    
  
         quoteAmount = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
         print("quoteAmount",quoteAmount);
         
         if(quoteAmount>10000000000):
               # 2W close position
            router.closePositionETH(routerAddress, quoteToken , quoteAmount=abs(quoteAmount), deadline = deadline, trader = userRobert.address)
            print("close position long")

        #  # withdraw margin
        #  withdrawableAmount = margin.getWithdrawable(marginAddress, userRobert.address);
        #  router.withdrawETH(routerAddress,quotetoken ,  withdrawableAmount)

        
         isLong = random.randint(0,1)
         quoteAmountRandom = random.randint(50,1000) * 1000000
        
         if(isLong): 
          
            router.openPositionETHWithWallet(routerAddress,0, marginAmount, quoteAmountRandom,userRobert.address, deadline, quoteToken );
            print("open long")

         else:

            router.openPositionETHWithWallet(routerAddress,1, marginAmount, quoteAmountRandom,userRobert.address, deadline, quoteToken );
            print("open short")
         
         count+=1
         print("count", count)

         time.sleep(120)  
         if(count == 5) :
              
               quoteAmount1 = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
               router.closePositionETH(routerAddress, quoteToken , quoteAmount=abs(quoteAmount1), deadline = deadline, trader = userRobert.address)
               count =0
               time.sleep(120)  
        
    
    


def main():
  
    
          
        try: 
            auto_trade();
            
        except  ValueError:
            print("something wrong ");

