# Apex-tarde-test
pip3 install -r requirements.txt

1. brownie networks add live arbitestnet host=https://rinkeby.arbitrum.io/rpc chainid=421611
  # brownie networks add live arbitrum host=https://arb1.arbitrum.io/rpc chainid=42161
2. brownie compile
3. brownie run amm.py --network arbitestnet
  # brownie run amm.py --network arbitrum

