
from socket import * 

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 发起连接　地址：服务端地址
sockfd.bind(('0.0.0.0',8888))

data = input("发送>>")

# 将内容变为bytes格式发送
sockfd.send(data.encode())

data = sockfd.recv(1024).decode()
print("收到消息:",data)

# 关闭套接字
sockfd.close()



