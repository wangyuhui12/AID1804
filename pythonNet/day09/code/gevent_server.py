import gevent
from gevent import monkey
# 需要在socket导入之前执行，改变socket的属性行为
monkey.patch_all()
from socket import *

# 套接字
def server(port):
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Connect from", addr)
        gevent.spawn(handle, c)

# 处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        else:
            print(data)
            c.send(b'Receive your message')
    c.close()


if __name__ == "__main__":
    server(8888)

