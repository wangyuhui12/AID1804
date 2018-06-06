
from socket import * 
from time import sleep

# 广播地址
dest = ('176.17.112.255', 8888)

s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字可以发送接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


while True:
    sleep(2)
    s.sendto("加油，russia!!".encode(), dest)

s.close()

