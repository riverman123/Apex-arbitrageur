import pandas as pd, pymysql
from sqlalchemy import create_engine


def db_to_csv(engin, query,file):
    df =pd.read_sql_query(query, engin)
    print("df: ", df)
    df= df.loc[:,['beta', 'debt_ratio' , 'liquidate_price' , 'profit_percent']]
    df.to_csv(file, index=False)



# DEFAULT_DATABASE = 'mysql+pymysql://admin:adminpaswordyyy@front-app-test-1.cktvqe5n4r6y.ap-southeast-1.rds.amazonaws.com:3306/apex'
# engin = create_engine(DEFAULT_DATABASE, pool_size=10, pool_recycle=7200,
#                               pool_pre_ping=True, encoding='utf-8')

#db_to_csv(engin, 'SELECT * FROM amm_profit_loss where id >= 269;', '1.csv')
df = pd.read_csv('./1.csv', usecols=['shared.user_id','symbol','timestamp', 'clzd_pz_open_fee', 'clzd_pz_funding_fee', 'shared.order_id', 'shared.order_type', 'shared.side','shared.symbol_str','shared.leaves_qty', 'order_specific.price', 'order_specific.qty', 'order_specific.order_status'])
#print(  (df['order_specific.order_status'] == 'New').head())
df_mask= df['order_specific.order_status']=='New'
df= df[df_mask]
df['timestamp']=pd.to_datetime(round(df['timestamp']/1000000), unit='s')
print(df)
print(df.to_csv('./2.csv'))
