from socket import *
from select import select 

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    #提交关注的ＩＯ时间，等待处理
    print("等待ＩＯ返回")
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            connfd,addr = r.accept()
            print("Connect from",addr)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print("Receive from",r.getpeername(),\
                    ":",data.decode())
                #将客户端套接字放到wlist中
                wlist.append(r)
    for w in ws:
        w.send("这是一条回复消息".encode())
        wlist.remove(w)

    for x in xs:
        if x is s:
            s.close()