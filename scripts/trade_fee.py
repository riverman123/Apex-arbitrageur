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
        # print(syncEvent)
        inputAmount = liquidateEvent["quoteAmount"]
        outputAmount = liquidateEvent["baseAmount"]
        isLong = (liquidateEvent["position"]["quoteSize"] < 0)
        if isLong:
            # input=BBB
            fee = liquidateEvent["position"]["baseSize"] * 0.001
        else:
            # input = usdc
            reserveBase = syncEvent['reserveBase']
            reserveQuote = syncEvent['reserveQuote']
            reserveBaseOld = reserveBase + outputAmount;
            reserveQuoteOld = reserveQuote - inputAmount;
            delay = inputAmount * reserveBaseOld / (reserveQuoteOld + inputAmount)
            
            fee = delay - outputAmount

    # 正常平仓方法
    else:
        # open/close position
        swapEvents = tx.events['(unknown)']
        if len(swapEvents) == 3:
            swapEvents = swapEvents[2]
        inputToken = swapEvents['topic2']
        # print('input token', inputToken)
        data = swapEvents['data']
        inputAmount = to_uint(Web3.toHex(data[0:32]), type_str="uint256")
        outputAmount = to_uint(Web3.toHex(data[33:65]), type_str="uint256")
        # print("inputAmount: ",inputAmount )
        # print("outputAmount: ",outputAmount )
        # BBB todo
        if inputToken == '0x0000000000000000000000008d5de6ac3732b8fbfc6d4843ac182eb725f3f741':
            fee = inputAmount * 0.001
        # usdc
        else:
            syncEvent = tx.events['Sync']
            reserveBase = syncEvent['reserveBase']
            reserveQuote = syncEvent['reserveQuote']
            reserveBaseOld = reserveBase + outputAmount;
            reserveQuoteOld = reserveQuote - inputAmount;
            # print("reserveBaseOld: ",reserveBaseOld )
            # print("reserveQuoteOld: ",reserveQuoteOld )
            # input usdc
            delay = inputAmount * reserveBaseOld / (reserveQuoteOld + inputAmount)

            fee = delay - outputAmount
    return fee

    # print("returnData",Web3.toText(result))


def main():
    print("-----------")
    # BBB
    # t = chain.get_transaction('0x952f0204f0cd4a565603e9e3991f63420e38eef38bef5fd8e0ffd26abf363d83')
    t = chain.get_transaction('0x598d7422e76aa535d021d301d5b3227409a05470f72cc30a4f7eeaab16026a2f')
    print(t.events)

    fee = get_trade_fee(t, False)
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