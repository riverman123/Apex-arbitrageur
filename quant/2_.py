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
balance = exchange.fetch_balance()
#print(balance)


# 限价单买
#order_info = exchange.create_limit_buy_order('CRV/USDT', 1, 2.1)  # 交易对、买卖数量、价格
# 市价单买
#order_info = exchange.create_market_buy_order('CRV/USDT', 1 )  # 交易对、买卖数量、价格
# print(order_info)
# id = order_info["info"]["ordId"]


# 获取所有未成交订单
print(exchange.privateGetTradeOrdersPending())

# 取消现货订单 
#cancel_result = exchange.cancel_order('420347848537030656',"CRV/USDT")
#print(cancel_result)

# 限价单卖出
#order_info = exchange.create_limit_sell_order('CRV/USDT', 1, 2.5)  # 交易对、买卖数量、价格
#print(order_info)
# 市价单卖出


# 永续合约杠杆买入
# order_info = exchange.create_order(symbol="CRV-USDT-SWAP",type="limit",side="buy",amount=10, price=1.2, params={
#     "tdMode":"isolated",
#     "ordType":"limit",
#     "posMode": "net_mode",
#      #"sz": 10    # 
#     })
# print(order_info)


# 取消合约订单
#cancel_result = exchange.cancel_order("421362326888136704","CRV-USDT-SWAP")

# =====其他操作
# 下市价单，自动撤单，合约相关操作，等等等等，都可以自动运行
# ETH-USD-SWAP
# ===== U 本位永续合约市价平仓
swap_market_order_info = exchange.private_post_trade_close_position({"instId":"ETH-USD-SWAP","mgnMode":"isolated"})
print(json.dumps(swap_market_order_info,sort_keys=True, indent=4, separators=(',', ': ')))
positions = exchange.fetch_position('ETH-USD-SWAP')
print(json.dumps(positions,sort_keys=True, indent=4, separators=(',', ': ')))

