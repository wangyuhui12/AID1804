
#tcp_server.py 
from socket import *  

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('176.17.112.159',9999))

#设置监听
sockfd.listen(5)


while True:
    print("Waiting for connect....")
    #阻塞等待客户端请求
    connfd,addr = sockfd.accept()
    print("Connect from",addr)


    while True:
        #接收消息
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive message:",data.decode())

        #发送消息　
        n = connfd.send(b'I love China')
        print("发送了%d个字节"%n)

    #关闭套接字
    connfd.close()
sockfd.close()


