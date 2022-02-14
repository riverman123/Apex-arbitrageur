from brownie import *
from brownie.convert import to_uint
from web3.main import Web3
from scripts import amm
import os
from config import config

SETTING = config.SETTING


# todo
def get_trade_fee(tx, is_liquidate=True):
    # 清算方法平仓
    fee = 0;
    if is_liquidate:
        # liquidate
        liquidateEvent = tx.events["Liquidate"]
        syncEvent = tx.events["Sync"]
        print(syncEvent)
        inputAmount = liquidateEvent["quoteAmount"]
        outputAmount = liquidateEvent["baseAmount"]
        isLong = (liquidateEvent["position"]["quoteSize"] < 0)
        if isLong:
            fee = liquidateEvent["position"]["baseSize"] * 0.001
        else:
            reserveBase = syncEvent['reserveBase']
            reserveQuote = syncEvent['reserveQuote']
            reserveBaseOld = reserveBase - inputAmount;
            reserveQuoteOld = reserveQuote + outputAmount;
            deltay = inputAmount * reserveQuoteOld / (reserveBaseOld + inputAmount)
            # print(deltay)
            fee = deltay - outputAmount

    # 正常平仓方法
    else:
        # open/close position
        swapEvents = tx.events['(unknown)']
        inputToken = swapEvents['topic2']
        data = swapEvents['data']
        inputAmount = to_uint(Web3.toHex(data[0:32]), type_str="uint256")
        outputAmount = to_uint(Web3.toHex(data[33:65]), type_str="uint256")
        # BBB
        if inputToken == '0x952f0204f0cd4a565603e9e3991f63420e38eef38bef5fd8e0ffd26abf363d83':
            fee = inputAmount * 0.001
        # usdc
        else:
            syncEvent = tx.events['Sync']
            reserveBase = syncEvent['reserveBase']
            reserveQuote = syncEvent['reserveQuote']
            reserveBaseOld = reserveBase - inputAmount;
            reserveQuoteOld = reserveQuote + outputAmount;
            deltay = inputAmount * reserveQuoteOld / (reserveBaseOld + inputAmount)
            # print(deltay)
            fee = deltay - outputAmount
    return fee

    # print("returnData",Web3.toText(result))


def main():
    print("-----------")
    # BBB
    # t = chain.get_transaction('0x952f0204f0cd4a565603e9e3991f63420e38eef38bef5fd8e0ffd26abf363d83')
    t = chain.get_transaction('0x1b5197ce40b99233aa1e350544db75147b80d8a4f0f11171e06ed604e3accdcf')
    print(t.events)
    liquidateEvent = t.events["Liquidate"]

    fee = get_trade_fee(t, True)
    print(fee)
    # syncEvent = t.events['Sync']
    # reserveBase = syncEvent['reserveBase']
    # reserveQuote =syncEvent['reserveQuote']
    # print(reserveBase)
    # print(reserveQuote)

    # swapEvents =  t.events['(unknown)']
    # print(swapEvents)
    # inputToken = swapEvents['topic2']
    # data = swapEvents['data']

    # inputAmount = Web3.toHex(data[0:32])
    # a = to_uint(inputAmount, type_str="uint256")
    # print("input: ", inputAmount)
    # print("a: ", a)
    # outputAmount = to_uint(Web3.toHex(data[33:65]), type_str="uint256")
    # print(outputAmount)
# 00000000000000000000000000000000000000000000000000000000d580fb80
# 000000000000000000000000000000000000000000000003610f56ff00445501