#!/usr/bin/python
# -*- coding: UTF-8 -*-
import eventlet
import json
import os 
import Module_Table as MT

def SearchSvrFunc(i):
    for key in Svr_Table:
        if key == i:
           return Svr_Table[key];

def ParsePacketReq(j_req):
    s = json.loads(j_req)
    return s

def CallSvrFunc(req,rsp):
    #载入对应模块
    svrno = req["SvrNo"]
    mm = __import__(MT.Module_Table[svrno])
    print "SvrFunc:"+mm.Svr_Table[svrno]
    eval("mm."+mm.Svr_Table[svrno])(req,rsp)

def handle(fd):
    print "client connected"
    while True:
        # pass through every non-eof line
        x = fd.readline()
        if not x: break
	req = ParsePacketReq(x)
        rsp = req
	CallSvrFunc(req,rsp)
        fd.write(json.dumps(rsp))
        fd.flush()
        print "echoed", rsp,
    print "client disconnected"

def server(ip='0.0.0.0',port=6000,poolnum=10000):
	print "server socket listening on port ",port
	server = eventlet.listen((ip, port))
	pool = eventlet.GreenPool(poolnum)
	while True:
	    try:
	        new_sock, address = server.accept()
	        print "accepted", address
	        pool.spawn_n(handle, new_sock.makefile('rw'))
	    except (SystemExit, KeyboardInterrupt):
			print "server quit!"
			break

#Main
if __name__ == "__main__":

	#daemon
	pid = os.fork()
	if(pid > 0):
   		exit(0)
	elif(pid == 0):
		print 'begin to work...'

	server()
