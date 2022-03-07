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


# =====获取账户余额
#balance = exchange.fetch_balance()
#print(balance)

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




# =====对比价差，策略



# ======下单



#

# 获取所有未成交订单
#print(exchange.privateGetTradeOrdersPending())


