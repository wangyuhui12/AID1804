

from socket import * 
import sys

# 从命令行输入ip和端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

#创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

#绑定服务端地址
sockfd.bind(ADDR)

#手法消息
while True:
    print("waiting for connecting...")
    data, addr = sockfd.recvfrom(1024)
    print("Receive from %s:%s" %(addr,data.decode()))
    sockfd.sendto('收到你的消息'.encode(), addr)

sockfd.close()




