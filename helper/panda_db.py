import pandas as pd, pymysql
from sqlalchemy import create_engine

def db_to_csv(engin, query,file):
    df =pd.read_sql_query(query, engin)
    print("df: ", df)
    df.to_csv(file, index=False)


DEFAULT_DATABASE = 'mysql+pymysql://admin:adminpaswordyyy@front-app-test-1.cktvqe5n4r6y.ap-southeast-1.rds.amazonaws.com:3306/apex'
engin = create_engine(DEFAULT_DATABASE, pool_size=10, pool_recycle=7200,
                              pool_pre_ping=True, encoding='utf-8')

db_to_csv(engin, 'SELECT * FROM amm_profit_loss;', '1.csv')
