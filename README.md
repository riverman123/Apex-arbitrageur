# Apex-tarde-test

The apex-arbitrageur is an arbitrage bot that can be run on AWS Lambda (works with free tier) or locally. The bot allows you to execute automated trading strategies between Apex Protocol (site, docs) and  CEX.
## install dependency
 pip3 install -r requirements.txt

## add network
 - testnet: brownie networks add live arbitestnet host=https://rinkeby.arbitrum.io/rpc chainid=421611
 - testnet1: brownie networks add live arbitestnet1 host=https://speedy-nodes-nyc.moralis.io/28c1b27b00698659dbd3958e/arbitrum/testnet chainid=421611
 -  arbi: brownie networks add live arbitrum host=https://arb1.arbitrum.io/rpc chainid=42161


## env
 python  3.9.6

## run 
1. brownie compile

2. brownie run arbitrageur.py --network arbitrum

 
  // for robert  

3. brownie run auto_trade_oracle.py --network arbitestnet1


