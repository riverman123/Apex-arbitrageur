from python_graphql_client import GraphqlClient
import time
# https://gist.github.com/AloftLab/7ec1901d1333bde4d21712566a4dfb20

# Start the client with an endpoint.
client = GraphqlClient(endpoint="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2")
class Calls:
   def QueryDB(self):
      query = '''
    {
    mints(where:{pair: "0x004375dff511095cc5a197a54140a24efef3a416", timestamp_gt: 1621353600}) { 
    id
    timestamp
   
    pair {
    
      token0 {
        name
      }
      token1 {
        name
      }
    } 
    sender
    amount0
    amount1
   } 
}
''' 
      return query
# As there is close to 20.000 tokens now when article is wrtitten am using range up to 21.000 as call is limited per 1000
my_list = [*range(1, 21000, 1000)]
print(my_list)
try:
      # calls queryDB with wanted statement (it can be changed based on documentation at uniswap api or graphql sandbox)
      data = client.execute(query=Calls().QueryDB())
    #   print(data)
      
# Extract details from gathered data.

      for token_details in data['data']["mints"]:
         id_ = token_details["id"]
        #  token0Price = token_details["token0Price"]
        #  token1Price = token_details["token1Price"]
        #  reserveUSD = token_details["reserveUSD"]
        #  reserveETH = token_details["reserveETH"]
         reserve0 = token_details["amount0"]
         reserve1 = token_details["amount1"]
         print("amount0: ", reserve0)
         print("amount1: ", reserve1)
         print("timestamp: ", token_details["timestamp"])


         # Time limit between calls - to avoid ban
         time.sleep(10)

except:
      pass

# now do something with data as store to DB or use for trading...