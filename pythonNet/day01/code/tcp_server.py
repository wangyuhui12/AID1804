
from socket import * 

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',5670))


#设置监听
sockfd.listen(5)

print("Waiting for connect...")

# 阻塞等待客户端请求
connfd,addr = sockfd.accept()
print("Connect from", addr)

# 接受消息
data = connfd.recv(1024)
print("Recevie message", data.decode('utf8'))

# 发送消息
n = connfd.send('I love Chinahaha.'.encode())
print("发送了%d个字节" %n)

# 关闭套接字
connfd.close()
sockfd.close()



