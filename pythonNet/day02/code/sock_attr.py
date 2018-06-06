

from socket import * 

s = socket()

#文件描述符
print(s.fileno())

# 套接字类型
print(s.type)

# 地址族类型
print(s.family)

# 设置套接字选项 让端口立即释放
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print(s.getsockopt(SOL_SOCKET, SO_REUSEADDR))

s.bind(('176.17.112.159', 8888))
# 获取套接字绑定的地址
print(s.getsockname())


s.listen(5)
connfd, addr = s.accept()

# 获取connfd链接的客户端地址
print(connfd.getpeername())

data = connfd.recv(1024)
print(data)

s.close()
