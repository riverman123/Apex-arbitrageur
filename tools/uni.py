from python_graphql_client import GraphqlClient
import time
# https://gist.github.com/AloftLab/7ec1901d1333bde4d21712566a4dfb20

# Start the client with an endpoint.
client = GraphqlClient(endpoint="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2")

class Calls:
   def QueryDB(self):
      query = '''
  {
  mints(where:{pair: "0x004375dff511095cc5a197a54140a24efef3a416", timestamp_gt: 1621353600, timestamp_lt: 1621785600}) { 
    id
    timestamp
   
    pair {
    
     reserve0
     reserve1
    } 
    sender
    amount0
    amount1
  }
  
   burns(where:{pair: "0x004375dff511095cc5a197a54140a24efef3a416", timestamp_gt: 1621353600, timestamp_lt: 1621785600}) { 
    id
    timestamp
     pair {
    
     reserve0
     reserve1
    } 
   
    sender
    amount0
    amount1
  }
  
  
}

  
''' 
      return query
# As there is close to 20.000 tokens now when article is wrtitten am using range up to 21.000 as call is limited per 1000
# my_list = [*range(1, 21000, 1000)]
# print(my_list)
try:
      # calls queryDB with wanted statement (it can be changed based on documentation at uniswap api or graphql sandbox)
      data = client.execute(query=Calls().QueryDB())
      #print(data['data']["mints"])
      
# Extract details from gathered data.
      print("-------mint---------")
      for mint_details in data['data']["mints"]:
        
         id_ = mint_details["id"]
         amount0 = mint_details["amount0"]
         amount1 = mint_details["amount1"]
         print("amount0: ", amount0)
         print("amount1: ", amount1)
         print("timestamp: ", mint_details["timestamp"])
         reserve0 = mint_details["pair"]["reserve0"]
         reserve1 = mint_details["pair"]["reserve1"]
         print("reserve0: ", reserve0)
         print("reserve1: ", reserve1)
         print("----------------")
      print("-------burn---------")
      for burn_details in data['data']["burns"]:
         id_ = burn_details["id"]
         print("id: ", id_)
         amount0 = burn_details["amount0"]
         amount1 = burn_details["amount1"]
         print("burn amount0: ", amount0)
         print("burn amount1: ", amount1)
         print("burn timestamp: ", burn_details["timestamp"])
         reserve0 = burn_details["pair"]["reserve0"]
         reserve1 = burn_details["pair"]["reserve1"]
         print("reserve0: ", reserve0)
         print("reserve1: ", reserve1)
         print("----------------")


         # Time limit between calls - to avoid ban
        #  time.sleep(10)

except:
      pass

# now do something with data as store to DB or use for trading...