import ccxt
from brownie import *
import os
from dotenv import load_dotenv
load_dotenv()

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


