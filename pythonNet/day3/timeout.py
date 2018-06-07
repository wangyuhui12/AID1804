from socket import *
from time import sleep,ctime 

s = socket()
s.bind(('127.0.0.1',9999))
s.listen(5)

#设置s的超时时间
s.settimeout(5)

while True:
    print("waiting for connect....")
    try:
        connfd,addr = s.accept()
    except timeout:
        sleep(2)
        print(ctime())
        continue

    print("Connect from",addr)
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.sendall(ctime().encode())
    connfd.close()
s.close()

