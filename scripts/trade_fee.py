from brownie import  *
import os
from config import config

SETTING = config.SETTING

def get_trade_fee(tx_id,is_liquidate=True):
    # 清算方法平仓
    if is_liquidate:
        result = chain.get_transaction(tx_id)
        events = result.events
        for i in logs:
            if i["topics"][0].hex() == "0xea474b265c6934eb153db1fc6a86ef56a505cbd6cc0e971ffb2d6cb4155369de":
                # 先把字符串转为bytes类型，Web3.toInt
                data = i["data"]
                # 切片是因为两个值在一起
                base_size = Web3.toInt(bytes.fromhex(data[2:66]))
                quote_size = Web3.toInt(bytes.fromhex(data[66:]))
                break
    # 正常平仓方法
    else:
        result = chain.get_transaction(tx_id)
        events = result.events
        for i in logs:
            if i["topics"][0].hex() == "0xfa2dda1cc1b86e41239702756b13effbc1a092b5c57e3ad320fbe4f3b13fe235":
                # 先把字符串转为bytes类型，Web3.toInt
                data = i["data"]
                # 切片是因为两个值在一起
                quote_size = Web3.toInt(bytes.fromhex(data[2:66]))
                base_size = Web3.toInt(bytes.fromhex(data[66:]))
                break
    return base_size


    # print("returnData",Web3.toText(result))
