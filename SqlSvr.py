# -*- coding: UTF-8 -*-
import sqlite3

#Sql模块
Svr_Table = {"3":"SqlSqlite3", #Sqlite3服务
}

def SqlSqlite3(req,rsp):
    print "service %s was called" % req["SvrNo"] 
    conn = sqlite3.connect("test.db")
    conn.execute("update test set id=id+1")
    conn.commit()
    cur = conn.cursor()
    cur.execute("select id from test")
    res = cur.fetchone()
    rsp["Id"] = res['id'];
    cur.close()
    conn.close()
    rsp["Result"] = "0000"

