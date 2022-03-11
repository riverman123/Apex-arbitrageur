# Apex-tarde-test
## install dependency
 pip3 install -r requirements.txt

## add network
 - testnet: brownie networks add live arbitestnet host=https://rinkeby.arbitrum.io/rpc chainid=421611
 -  arbi: brownie networks add live arbitrum host=https://arb1.arbitrum.io/rpc chainid=42161

## run 
1. brownie compile

2. brownie run arbitrageur.py --network arbitrum

