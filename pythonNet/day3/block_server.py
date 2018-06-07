from socket import *
from time import sleep,ctime 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)

#将s设置为非阻塞
s.setblocking(False)

while True:
    print("waiting for connect....")
    try:
        connfd,addr = s.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue

    print("Connect from",addr)
    #connfd.setblocking(False)
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.sendall(ctime().encode())
    connfd.close()
s.close()

