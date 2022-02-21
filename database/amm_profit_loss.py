from helper.db_session import execute,fetch_to_dict


# 查询用户钱包记录  type 18 为返还手续费记录
def insert_records(beta, debt_ratio, liquidity_ratio, base_reserves_begin, market_price_begin, user_a_position,
                   liquidate_price, user_b_position, market_price_after_b, profit_loss,profit_percent):
    sql = 'INSERT into amm_profit_loss (beta,debt_ratio,liquidity_ratio,base_reserves_begin,market_price_begin,user_a_position,liquidate_price,user_b_position,market_price_after_b,profit_loss,profit_percent) VALUES(:beta,:debt_ratio,:liquidity_ratio,:base_reserves_begin,:market_price_begin,:user_a_position,:liquidate_price,:user_b_position,:market_price_after_b,:profit_loss,:profit_percent)'
    results = execute(sql=sql, params={'beta': beta, 'debt_ratio': debt_ratio, 'liquidity_ratio': liquidity_ratio,
                                       'base_reserves_begin': base_reserves_begin,
                                       'market_price_begin': market_price_begin, 'user_a_position': user_a_position,
                                       'liquidate_price': liquidate_price, 'user_b_position': user_b_position,
                                       'market_price_after_b': market_price_after_b, 'profit_loss': profit_loss,'profit_percent':profit_percent})
    return results

def get_records(id_begin,id_end):
    sql = 'SELECT * FROM amm_profit_loss where id >= :id_begin and id <= :id_end'
    results = fetch_to_dict(sql=sql,params={'id_begin':id_begin,'id_end':id_end},fecth='all')
    return results