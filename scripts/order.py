import os
import json
from dotenv import load_dotenv
load_dotenv()


PRIVATE_KEY_USER = os.getenv("PRIVATE_KEY_USER")
PRIVATE_KEY_ROBOT = os.getenv("PRIVATE_KEY_ROBOT")
APIKEY = os.getenv("APIKEY")
SECRET = os.getenv("SECRET")
PASSWORD = os.getenv("PASSWORD")
import ccxt


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
#balance = exchange.fetch_balance()
#print(balance)
# check balance
# check margin ratio  marginFraction


#balance 两边仓位

# =====获取cex合约行情
mes = exchange.fetch_ticker("CRV-USD-SWAP")
print(json.dumps(mes,sort_keys=True, indent=4, separators=(',', ': ')))

# bid 买 , ask 卖
bidPrice=mes['bid']
baseVolume=mes['baseVolume']
askPrice=mes['ask']
askVolume=mes['askVolume']
print(bidPrice)
print(baseVolume)
print(askPrice)
print(askVolume)


# =====获取apex合约行情
#FtxUsdBalance
#FtxMarginRatio
#FtxMarginRatio
#FtxPnL



# =====对比价差，策略
spread = (apexprice - okexprice)/okexprice
amount =  sqrt( ammPrice*(1+ 0.001)* baseAssetReserve * quoteAssetReserve) - quoteAssetReserve
if spread<= -0.005 :  
    # open long position on perp
    # open short on ftx
   let ftxPositionSizeAbs = amount.div(ftxPrice).abs().round(3) 
   exchangedPositionSize = apex.openPostion(amount, LEVERAGE, Side.BUY)
   ftx.openPosition(exchangedPositionSize, Side.SELL)

else if spread>= 0.005: 
  #  open short on ftx 
  #  open long on perp
   let ftxPositionSizeAbs = amount.div(ftxPrice).abs().round(3) 
   exchangedPositionSize = apex.openPostion(amount, LEVERAGE, Side.SELL)
   ftx.openPosition(exchangedPositionSize, Side.BUY)
 





# ======下单



#

# 获取所有未成交订单
#print(exchange.privateGetTradeOrdersPending())


