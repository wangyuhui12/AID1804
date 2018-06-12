from socket import *

#确保和另一端使用相同的套接字文件
sock_file = "./sock_file"

#本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)
#链接另外一端
sockfd.connect(sock_file)

#发收消息
while True:
    msg = input(">>")
    if msg:
        sockfd.send(msg.encode())
        print(sockfd.recv(1024).decode())
    else:
        break 
sockfd.close()