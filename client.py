# -*- coding: UTF-8 -*-
import socket
import thread

def SendRecvFromSvr(sock,num):
    for i in xrange(num):
        sock.send('{"SvrNo":"1"}\n')
        print sock.recv(1024)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6000))
    SendRecvFromSvr(sock,200000)
    sock.close()
