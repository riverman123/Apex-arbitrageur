import ccxt
from brownie import *
import os
import json
import math
from scripts import priceOracle, amm, margin, router
from config import config
from dotenv import load_dotenv
load_dotenv()


PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
userRobert = accounts.add(private_key=PRIVATE_KEY_ROBOT)

APIKEY = os.getenv("APIKEY")
SECRET = os.getenv("SECRET")
PASSWORD = os.getenv("PASSWORD")


# =交易所配置
OKEX_CONFIG = {
    'apiKey': APIKEY,
    'secret': SECRET,
    'password': PASSWORD,
    'timeout': 3000,
    'rateLimit': 10,
    #  'hostname': 'okex.me',  # 无法fq的时候启用
    'enableRateLimit': False}

# =====创建ccxt交易所
exchange = ccxt.okex(OKEX_CONFIG)   # 其他交易所为huobipro, binance, okex


# =====获取okex账户余额
balance = exchange.fetch_balance()
print(balance)
# check balance
# check margin ratio  marginFraction


# balance 两边仓位

# =====获取cex合约行情
def getCexPrice():
    mes = exchange.fetch_ticker("ETH-USD-SWAP")
    print(json.dumps(mes, sort_keys=True, indent=4, separators=(',', ': ')))
    # bid 买 , ask 卖
    bidPrice = mes['bid']
    baseVolume = mes['baseVolume']
    askPrice = mes['ask']
    askVolume = mes['askVolume']
    print("cexprice: ", bidPrice)
    print(baseVolume)
    print(askPrice)
    print(askVolume)
    cexPrice = bidPrice
    return cexPrice


# =====获取apex合约行情
def getDexPrice():
    # ammAddress = config.CONTRACT_ADDRESS["pairs"]["ETH/USD"]["amm"]
    ammAddress = "0x3eb6ccE3A2213C013eD9345faEbE2ef56c33609A"
    apexPrice = priceOracle.getMarkPrice(ammAddress)
    print("apex price: ", apexPrice)
    return apexPrice
    # FtxUsdBalance
    # FtxMarginRatio
    # FtxMarginRatio
    # FtxPnL


def arbitrate(apexprice, cexPrice):
    # =====对比价差，策略
    spread = (apexprice - cexPrice)/cexPrice
    print("spread: ", spread)
    reserves = amm.getReserves("0x3eb6ccE3A2213C013eD9345faEbE2ef56c33609A")
    print(reserves)
    # 0.05%
    # amount =  math.sqrt( apexprice*(1+ 0.001)* reserves[0] * reserves[1]/10**24) - reserves[1]/10**6
    amount = 10
    print("amount: ", amount)
    baseToken = amm.getBaseToken("0x3eb6ccE3A2213C013eD9345faEbE2ef56c33609A")
    quoteToken = amm.getQuoteToken(
        "0x3eb6ccE3A2213C013eD9345faEbE2ef56c33609A")
    print("baseToken: ", baseToken)
    if spread <= -0.005:
        #     # open long position on perp
        #     # open short on ftx
      # ftxPositionSizeAbs = amount/cexPrice * 2
        # print("- position size: ", ftxPositionSizeAbs)
        #

        tx = router.openPositionETHWithWallet(side=0, marginAmount=0.02,
                                       quoteAmount=int(abs(amount)) + 1,
                                       trader=userRobert.address, deadline=1957515898, baseToken=baseToken, quoteToken=quoteToken)
        print("-tx ", tx)
        position_info = margin.getPosition(userRobert.address)
        print("-开仓仓位：", position_info)

      # exchange.openPosition(exchangedPositionSize, Side.SELL)

        order_info = exchange.create_order(symbol="ETH-USD-SWAP", type="market", side="sell", amount=amount, params={
            "tdMode": "isolated",
            "ordType": "market",
            "posMode": "net_mode",
            #"sz": 10    #
        })
        print("- cex order_info: ", order_info)

    elif spread >= 0.005:
        #   #  open short on ftx
        #   #  open long on perp
        #    let ftxPositionSizeAbs = amount.div(ftxPrice).abs().round(3)
        #    exchangedPositionSize = apex.openPostion(amount, LEVERAGE, Side.SELL)
        #    ftx.openPosition(exchangedPositionSize, Side.BUY)

      #  ftxPositionSizeAbs = amount/cexPrice * 2
      #  print("+ position size: ", ftxPositionSizeAbs)
        #

        # tx = router.openPositionETHWithWallet(side=1, marginAmount=0.02,
        #                                quoteAmount=int(abs(amount)) + 1,
        #                                trader=userRobert.address, deadline=1957515898, baseToken=baseToken, quoteToken=quoteToken)
        # print("+tx ", tx)
        position_info = margin.getPosition(userRobert.address)
        print("+开仓仓位：", position_info)
      # exchange.openPosition(exchangedPositionSize, Side.SELL)

        # order_info = exchange.create_order(symbol="ETH-USD-SWAP", type="market", side="buy", amount=amount, params={
        #     "tdMode": "isolated",
        #     # "ordType":"market",
        #     "posMode": "net_mode",
        #     #"sz": 10    #
        # })
        #print("+ cex order_info: ", order_info)
        positions = exchange.fetch_position('ETH-USD-SWAP')
        print(json.dumps(positions,sort_keys=True, indent=4, separators=(',', ': ')))

# ======下单


#

# 获取所有未成交订单
# print(exchange.privateGetTradeOrdersPending())


def main():
    cexPrice = getCexPrice()
    dexPrice = getDexPrice()
    arbitrate(cexPrice, dexPrice)
