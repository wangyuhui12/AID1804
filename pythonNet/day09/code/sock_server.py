
from socketserver import *

# 创建多进程tcp并发

# 创建进程tcp服务器类
# class Server(ForkingMixIn, TCPServer):
#     pass
class Server(ForkingTCPServer):
    pass

#　具体请求处理类
class Handler(StreamRequestHandler):

    def handle(self):
        # self.request 相当于　accept 创建的套接字
        print("Connect from", self.request.getpeername())
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            print(data)
            self.request.send(b"Receive your message")


# 生成服务器对象， 传入addr 和 具体处理类
server = Server(('0.0.0.0', 8888), Handler)

#启动服务器
server.serve_forever()


