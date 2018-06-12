from socket import *
from select import * 

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))
s.listen(5)

#创建epoll对象
p = epoll()
# 建立通过fileno查找IO对象的地图
fdmap = {s.fileno():s}
#添加关注
p.register(s,EPOLLIN | EPOLLERR)

while True:
    #进行监控
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #注册新的套接字
            p.register(c,EPOLLIN)
            #维护地图更新
            fdmap[c.fileno()] = c 
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send('收到了'.encode())
