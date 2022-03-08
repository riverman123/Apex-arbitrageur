import ccxt
from brownie import *
import os
import json
from scripts import priceOracle, amm, margin, router, initCex
from config import config
from dotenv import load_dotenv
load_dotenv()

ammAddress = "0x3eb6ccE3A2213C013eD9345faEbE2ef56c33609A"
perp_pair = "ETH-USD-SWAP"
spread_range = 0.05
leverage = 3
marginAmount = 0.02

# =====获取cex合约行情
def getCexPrice():
    mes = exchange.fetch_ticker(perp_pair)
    print(json.dumps(mes, sort_keys=True, indent=4, separators=(',', ': ')))
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


# =====获取apex合约行情
def getDexPrice():
    apexPrice = priceOracle.getMarkPrice(ammAddress)
    print("apex price: ", apexPrice)
    return apexPrice
    # FtxUsdBalance
    # FtxMarginRatio
    # FtxMarginRatio
    # FtxPnL


def arbitrate(apexprice, cexPrice):
    # =====对比价差，执行策略
    spread = (apexprice - cexPrice)/cexPrice
    print("spread: ", spread)
    reserves = amm.getReserves(ammAddress)
    print(reserves)
    # 0.05%
    # amount =  math.sqrt( apexprice*(1+ 0.001)* reserves[0] * reserves[1]/10**24) - reserves[1]/10**6
    amount = 10
    print("amount: ", amount)
    baseToken = amm.getBaseToken(ammAddress)
    quoteToken = amm.getQuoteToken(ammAddress)
    print("baseToken: ", baseToken)
    if spread <= -1* spread_range:
        print("dex open long , cex open short")
      # ftxPositionSizeAbs = amount/cexPrice * 2
        # print("- position size: ", ftxPositionSizeAbs)
        #

        tx = router.openPositionETHWithWallet(side=0, marginAmount=marginAmount,
                                       quoteAmount=int(abs(amount)) + 1,
                                       trader=userRobert.address, deadline=1957515898, baseToken=baseToken, quoteToken=quoteToken)
        print("tx hash ", tx)
        position_info = margin.getPosition(userRobert.address)
        print("position：", position_info)

        # cex open short
        order_info = exchange.create_order(symbol=perp_pair, type="market", side="sell", amount=amount, params={
            "tdMode": "isolated",
            "ordType": "market",
            "posMode": "net_mode",
            #"sz": 10    
        })
        print("- cex order_info: ", order_info)

    elif spread >= spread_range:
        print("dex open short , cex open long")
        #    let ftxPositionSizeAbs = amount.div(ftxPrice).abs().round(3)
        #    exchangedPositionSize = apex.openPostion(amount, LEVERAGE, Side.SELL)
        #    ftx.openPosition(exchangedPositionSize, Side.BUY)

      #  ftxPositionSizeAbs = amount/cexPrice * 2
      #  print("+ position size: ", ftxPositionSizeAbs)
        #

        tx = router.openPositionETHWithWallet(side=1, marginAmount=marginAmount,
                                       quoteAmount=int(abs(amount)) + 1,
                                       trader=userRobert.address, deadline=1957515898, baseToken=baseToken, quoteToken=quoteToken)
        print("tx hash ", tx)
        position_info = margin.getPosition(userRobert.address)
        print("+position：", position_info)
        # cex open short
        order_info = exchange.create_order(symbol=perp_pair, type="market", side="buy", amount=amount, params={
            "tdMode": "isolated",
            "ordType":"market",
            "posMode": "net_mode",
            #"sz": 10    #
        })
        print("+ cex order_info: ", order_info)

    positions = exchange.fetch_position(perp_pair)
    print("cex position",json.dumps(positions,sort_keys=True, indent=4, separators=(',', ': ')))


#

# 获取所有未成交订单
# print(exchange.privateGetTradeOrdersPending())


def main():
    cexPrice = getCexPrice()
    dexPrice = getDexPrice()
    arbitrate(cexPrice, dexPrice)
