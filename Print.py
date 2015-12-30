# -*- coding: UTF-8 -*-

#Print模块
Svr_Table = {"1":"Print1", #服务序号1
             "2":"Print2", #服务序号2
}

def Print1(req,rsp):
    print "service %s was called" % req["SvrNo"] 
    rsp["Result"] = "0000"

def Print2(req,rsp):
    print "service %s was called" % req["SvrNo"] 
