from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from config import config
import sys
import csv


def _db_init():
    engin = create_engine(config.DEFAULT_DATABASE, pool_size=10, pool_recycle=7200,
                              pool_pre_ping=True, encoding='utf-8')
    session_factory = sessionmaker(bind=engin)
    session = session_factory()
    return session


# 字典的方式返回数据：[{},{}]
def fetch_to_dict(sql, params={}, fecth='one'):
    session = _db_init()
    resultProxy = session.execute(sql, params)
    if fecth == 'one':
        result_tuple = resultProxy.fetchone()
        if result_tuple:
            result = dict(zip(resultProxy.keys(), list(result_tuple)))
        else:

            return None
    else:
        result_tuple_list = resultProxy.fetchall()
        if result_tuple_list:
            result = []
            keys = resultProxy.keys()
            for row in result_tuple_list:
                result_row = dict(zip(keys, row))
                result.append(result_row)
        else:
            return None
    session.close()
    return result


# 执行单条语句（update,insert）
def execute(sql, params={}):
    session = _db_init()
    try:
        cursor = session.execute(sql, params)
        session.commit()
        session.close()
        return cursor.lastrowid
    except Exception as e:
        session.rollback()
        raise e


def writeExcel(result):
    c = csv.writer(open("temp.csv","wb"))
    c.writerow(result)
