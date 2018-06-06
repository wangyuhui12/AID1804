
#tcp_client.py
from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接 地址:服务端地址
sockfd.connect(('192.168.42.60', 8888))


while True:
    data = input('发送>>')
    if not data:
        break
    #将内容变为bytes格式发送
    sockfd.send(data.encode())

    data = sockfd.recv(1024).decode()
    print("收到消息:",data)

sockfd.close()
