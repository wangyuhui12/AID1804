
# fork tcp并发
from socket import *
import os, sys
import signal

#服务器地址
HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST, PORT)

# 处理客户端请求函数
def client_handle(c):
    print("子进程处理客户端:", c.getpeername())
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'Receive your message')


# 创建tcp监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen to 8888....")
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    # 有客户端连接创建子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建子进程失败")
    elif pid == 0:
        s.close() # 子进程不需要监听套接字
        #调用函数处理客户请求
        client_handle(c)
        # 子进程处理完客户端请求一定要退出
        c.close()
        sys.exit(0)
    else:
        c.close()# 父进程不需要和客户端交互
        continue

