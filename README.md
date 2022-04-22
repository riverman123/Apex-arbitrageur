# Apex-tarde-test

The apex-arbitrageur is an arbitrage bot that can be run on AWS Lambda (works with free tier) or locally. The bot allows you to execute automated trading strategies between Apex Protocol (site, docs) and  CEX.
## install dependency
 pip3 install -r requirements.txt

## add network
 - testnet: brownie networks add live arbitestnet host=https://rinkeby.arbitrum.io/rpc chainid=421611
 -  arbi: brownie networks add live arbitrum host=https://arb1.arbitrum.io/rpc chainid=42161

## run 
1. brownie compile

2. brownie run arbitrageur.py --network arbitrum

3. brownie run auto_trade.py --network arbitestnet

