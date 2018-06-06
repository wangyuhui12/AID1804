
from socket import * 
from time import sleep

def get_text(filename):
    with open(filename) as f:
        text1 = f.read()

    return text1

ADDR = ('192.168.42.60', 8888)

sockfd = socket(AF_INET, SOCK_STREAM)

sockfd.bind(ADDR)

# # 设置套接字可以发送接受广播
# sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sockfd.listen(5)


while True:
    print("Waiting for connect...")

    connfd, addr = sockfd.accept()

    while True:

        data = connfd.recv(1024)
        if not data:
            break
        print("Receive message:", data.decode())

        text = get_text('test.txt')
        n = connfd.send(text.encode())

    connfd.close()
sockfd.close()












