'''
    HTTPServer 第二版
'''
from socket import *
from threading import Thread
import time

ADDR = ('0.0.0.0', 8000)
# 存放静态页面的目录
STATIC_DIR = "./static"

# httpserver类,封装服务器功能


class HTTPServer(object):
    def __init__(self, addr):
        # 套接字创建
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)
        # 为对象添加一些属性
        self.name = "HttpServer"
        self.port = 8000
        self.address = addr

    #　不断的监听客户端的连接请求，创建新的线程处理
    def server_forever(self):
        print("Listen to port 8000....")
        while True:
            connfd, clientAddr = self.sockfd.accept()
            #　创建新的线程处理具体请求
            clientThread = Thread(target=self.handleRequest, args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    def handleRequest(self, connfd):
        #　接受客户端请求
        request = connfd.recv(4096)
        print("******8")
        #　按行切割
        requestHeadlers = request.splitlines()
        # 请求行
        print(connfd.getpeername, ":", requestHeadlers[0])
        #　获取具体请求
        getRequest = str(requestHeadlers[0]).split(' ')[1]


        #　访问静态网页
        if getRequest[-3:] != ".py":
            if getRequest == '/':
                getFilename = STATIC_DIR + "/index.html"
            else:
                getFilename = STATIC_DIR + getRequest

            try:
                f = open(getFilename)
            except Exception:
                #　没有找到页面
                responseHeaders = "HTTP/1.1 404 not found\r\n" # 响应行
                responseHeaders += "\r\n"   # 响应头
                responseBody = "====Sorry, the page not found===="  #　响应体
            else:
                responseHeaders = "HTTP/1.1 200 OK\r\n" # 响应行
                responseHeaders += "\r\n"   # 响应头
                responseBody = f.read() #　响应体   
            finally:
                response = responseHeaders + responseBody
                connfd.send(response.encode())         
        #　访问后台程序
        else:
            #　通过函数得到响应体
            responseBody = self.application()

            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            response = responseHeaders + responseBody
            connfd.send(response.encode())

        connfd.close()

    # 获取你要使用的外部函数，变为属性
    def setApp(self, application):
        self.application = application



#　后台程序 
def app():
    return "\n====假设这是一个很复杂的程序，你得到了一个很牛逼的内容===\n%s" %time.ctime()





if __name__ == "__main__":
    httpd = HTTPServer(ADDR)
    httpd.setApp(app)
    #　启动服务器
    httpd.server_forever()
