import pandas as pd
from database import amm_profit_loss

def db_to_csv():
    data = amm_profit_loss.get_records(362,449)
    beta_list = []
    liquidity_ratio_list = []
    profit_loss_list = []
    profit_percent_list = []
    for i in data:
        beta = i['beta']
        if not (beta in beta_list):
            beta_list.append(beta)
        liquidity_ratio = i['liquidity_ratio']
        if not (liquidity_ratio in liquidity_ratio_list):
            liquidity_ratio_list.append(liquidity_ratio)
        profit_loss_list.append(i['profit_loss'])
        profit_percent_list.append(i['profit_percent'])
    n = len(liquidity_ratio_list)  # 大列表中几个数据组成一个小列表
    profit_loss_list_data = [profit_loss_list[i:i + n] for i in range(0, len(profit_loss_list), n)]
    profit_percent_list_data = [profit_percent_list[i:i + n] for i in range(0, len(profit_percent_list), n)]

    print(beta_list)
    print(liquidity_ratio_list)
    print(profit_percent_list_data)

    df = pd.DataFrame(profit_percent_list_data,
    index = beta_list,
    columns = liquidity_ratio_list)

    df.to_csv('2.csv')
db_to_csv()