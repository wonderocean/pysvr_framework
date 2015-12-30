#!/user/bin/env python
#-*- encoding:utf-8 -*-
import socket
import thread,threading

sockIndex = 1

def connToServer (conn):
    global sockIndex
    print sockIndex
    sockIndex = sockIndex + 1
    for i in xrange(10):
        conn.send('{"SvrNo":"3"}\n')
        while True:
        #等待服务端返回数据，并输出
            rev = conn.recv(1024)
            print 'get server msg:' + str(rev)
            break

if __name__ == "__main__":
    threads = []
    times = 20000
    #创建一个socket连接到127.0.0.1:8081，并发送内容
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 6000))
    #并发
    for i in xrange(times):
        t = threading.Thread(target=connToServer(conn))
        threads.append(t)
    for i in xrange(times):
        threads[i].start()
    for i in xrange(times):
        threads[i].join()

    conn.close()



