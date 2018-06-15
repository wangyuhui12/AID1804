
from socket import *
from threading import Thread 
import sys
from time import sleep

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

def client_handle(c):
    print("Connect from", c.getpeername())
    while True:
        # try:
        data = c.recv(1024).decode()
        print(data)
        if not data:
            break
        print(data)
        c.send("Receive youmessage".encode())
        # except Exception as e:
        #     print(e)
        #     break
    c.close()   


# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

        # 创建线程， 绑定函数执行具体客户端请求
    t = Thread(target=client_handle, args=(c,))
    # 设置非阻塞，主线程退出，分支线程也会退出
    t.setDaemon(True)
    # t.daemon = True
    t.start()
    

