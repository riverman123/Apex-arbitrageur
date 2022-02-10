from brownie import  *

from dotenv import load_dotenv
load_dotenv()
# my_address = os.getenv("ACCOUNT_ADDRESS")
# private_key = os.getenv("PRIVATE_KEY")

def main():
  
    IAmm = interface.IAmm("0x357B185F7D472b0bC7b9a8dE3A26d3404b26acCa")

    reserve =  IAmm.getReserves()
    print(reserve)
    userA = accounts.add(private_key="0x5921059e276bae2e61d8e5ade6d6a026cce953344d3b9f0df218ef9ecd90ac58")
    IAmm.rebaseFree({"from": userA})
    reserve =  IAmm.getReserves()
    print(reserve)