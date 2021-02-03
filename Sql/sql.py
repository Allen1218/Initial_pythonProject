# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:08:05 2019
@author: dell
"""

import cx_Oracle as db


def connectOracle():
    ORACLE_HOST = 'ksmesi-scan.luxshare.com.cn'
    ORACLE_PORT = 1521
    #ORACLE_SID = 'xe'

    SERVICE_NAME = 'ksmesi'
    ORACLE_USER = 'twprod'
    ORACLE_PASSWORD = 'twprod'
    # dsn:data source name
    #dsn = db.makedsn(ORACLE_HOST, ORACLE_PORT, ORACLE_SID)
    dsn = db.makedsn(ORACLE_HOST, ORACLE_PORT, SERVICE_NAME)
    con = db.connect(ORACLE_USER, ORACLE_PASSWORD, dsn)
    # oracleDB = cx_Oracle.connect('ProxyPool/123456@localhost:1521/xe')    #用户密码主机端口SID
    return con


def query(con):
    cur = con.cursor()
    sql = "select table_name from all_tables where owner='PROXYPOOL'"
    cur.execute(sql)
    print("\n>>> " + sql)
    rs = cur.fetchall()
    for list in rs:
        print(list)  # 输出指定用户下的所有表名

    sql = "select * from proxylist"
    cur.execute(sql)
    rs = cur.fetchall()
    print("\n>>> " + sql)
    for list in rs:
        print(list)  # 输出该表中的信息
    cur.close()


def insert(con):
    sql = "INSERT INTO PROXYLIST(TYPE,DATA) VALUES(:TYPELIST,:DATALIST)"
    recodeList = [{"TYPELIST": 'http', "DATALIST": '112.87.71.44:9999'},
                  {"TYPELIST": 'http', "DATALIST": '61.178.149.237:59042'}]
    cur = con.cursor()
    cur.executemany(sql, recodeList)
    con.commit()  # 将事务交付给数据库进行处理，使用cursor对数据库进行操作后必须进行该操作
    cur.close()


if __name__ == '__main__':
    con = connectOracle()
    #insert(con)
    #query(con)

    curs = con.cursor()
    sql = 'select * from TwUnitFAJudgeInfo'
    curs.execute(sql)

    for result in curs:
        print(result)

    curs.close()

    con.close()