import ccxt
from brownie import *
import os
import json
from scripts import priceOracle, amm, margin, router
from config import config
from dotenv import load_dotenv
import time
load_dotenv()

ammAddress = "0x3eb6ccE3A2213C013eD9345faEbE2ef56c33609A"
marginAddress = "0x2fE7fC775D8eD8Da9fc1eEbfBAbfb57304448A03"
perp_pair = "ETH-USD-SWAP"
spread_range_open = 0.05   # 5%
spread_range_close = 0.01  # 1%
leverage = 3
marginAmount = 0.02  # eth
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userRobert = accounts.add(private_key=PRIVATE_KEY_ROBOT)

hasPosition = False;


def initCex():

  APIKEY = os.getenv("APIKEY")
  SECRET = os.getenv("SECRET")
  PASSWORD = os.getenv("PASSWORD")    
  OKEX_CONFIG = {
      'apiKey': APIKEY,
      'secret': SECRET,
      'password': PASSWORD,
      'timeout': 3000,
      'rateLimit': 10,
      #  'hostname': 'okex.me',  # wall
      'enableRateLimit': False}

  #ccxt
  exchange = ccxt.okex(OKEX_CONFIG)   # huobipro, binance, okex
  return exchange

def getCexPrice(exchange):
    mes = exchange.fetch_ticker(perp_pair)
    #print(json.dumps(mes, sort_keys=True, indent=4, separators=(',', ': ')))
    # bid 买 , ask 卖
    bidPrice = mes['bid']
    baseVolume = mes['baseVolume']
    askPrice = mes['ask']
    askVolume = mes['askVolume']
    print("cexprice: ", bidPrice)
    # print(baseVolume)
    # print(askPrice)
    # print(askVolume)
    cexPrice = bidPrice
    return cexPrice

def getDexPrice():
    apexPrice = priceOracle.getMarkPrice(ammAddress)
    print("apex price: ", apexPrice)
    return apexPrice
    # FtxUsdBalance
    # FtxMarginRatio
    # FtxMarginRatio
    # FtxPnL


def arbitrate( exchange , hasPosition):

    # =====get cex balance
    balance = exchange.fetch_balance()
    #print(balance['total'])
    # Check  balance (USD)
    # Check margin ratio
    # check pnl
    
    reserves = amm.getReserves(ammAddress)
    #print("reserve: ", reserves)
    cexPrice = getCexPrice(exchange)
    dexPrice = getDexPrice()
    spread = (dexPrice - cexPrice)/cexPrice
    print("-------spread: ", spread)

    
    baseToken = amm.getBaseToken(ammAddress)
    quoteToken = amm.getQuoteToken(ammAddress)
    if abs(spread)< spread_range_close :
        if(hasPosition):
    
            #close dex position
            quoteAmount = margin.getPositionAccurate(marginAddress ,userRobert.address)[1]
            margin.closePosition(marginAddress ,userRobert.address, quoteAmount=abs(quoteAmount))
            # withdraw margin
            withdrawable = margin.getWithdrawable(marginAddress, userRobert.address);
            margin.removeMargin(marginAddress, userRobert.address, userRobert.address,  withdrawable)

            # close cex position 
            exchange.private_post_trade_close_position({"instId":perp_pair,"mgnMode":"isolated"})
            hasPosition = False
            print("close position")

    elif spread <= -1* spread_range_open:
        if hasPosition==False:
            print("dex open long , cex open short")
            
            # print("- position size: ", ftxPositionSizeAbs)
            #
            quoteAmount = marginAmount * getDexPrice()* leverage
            tx = router.openPositionETHWithWallet(side=0, marginAmount=marginAmount,
                                        quoteAmount=quoteAmount,
                                        trader=userRobert.address, deadline=1957515898, baseToken=baseToken, quoteToken=quoteToken)
            print("tx hash ", tx)
            position_info = margin.getPositionAccurate(marginAddress, userRobert.address)
            print("position：", position_info)

            # cex open short
            amount1 =  marginAmount*leverage * cexPrice/10
            order_info = exchange.create_order(symbol=perp_pair, type="market", side="sell", amount= amount1, params={
                "tdMode": "isolated",
                "ordType": "market",
                "posMode": "net_mode",
                #"sz": 10    
            })
            print("- cex order_info: ", order_info['symbol'])
            positions = exchange.fetch_position(perp_pair)
            print("cex position margin ratio ", positions["marginRatio"])
            print("cex position liquidate price ", positions["liquidationPrice"])
            hasPosition = True

    elif spread >= spread_range_open:
        if hasPosition==False:
            print("dex open short , cex open long")
            #
            quoteAmount = marginAmount * getDexPrice()* leverage
            tx = router.openPositionETHWithWallet(side=1, marginAmount=marginAmount,
                                        quoteAmount= quoteAmount ,
                                        trader=userRobert.address, deadline=1957515898, baseToken=baseToken, quoteToken=quoteToken)
            print("tx hash ", tx)
            position_info = margin.getPositionAccurate(marginAddress, userRobert.address)
            print("+position：", position_info)
            # cex open short
            amount1 =  marginAmount*leverage * cexPrice/10
            order_info = exchange.create_order(symbol=perp_pair, type="market", side="buy", amount= amount1, params={
                "tdMode": "isolated",
                "ordType":"market",
                "posMode": "net_mode",
                #"sz": 10    #
            })
            print("+ cex order_info id : ", order_info['symbol'])
            positions = exchange.fetch_position(perp_pair)
            print("cex position margin ratio ", positions["marginRatio"])
            print("cex position liquidate price ", positions["liquidationPrice"])
            hasPosition = True
    time.sleep(10)
    


#

# 获取所有未成交订单
# print(exchange.privateGetTradeOrdersPending())


def main():
    while True:
      #time.sleep(10)
      exchange = initCex()
      hasPosition = False;
      arbitrate(exchange, hasPosition )
