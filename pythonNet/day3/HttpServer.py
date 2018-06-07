from socket import *

#处理客户请求，返回响应
def handleClient(connfd):
    request = connfd.recv(4096)
    # print("*************")
    # print(request)
    # print("*************")
    requestHeadlers = request.splitlines()
    for line in requestHeadlers:
        print(line)

    try:
        f = open("index.html",'r')
    except IOError:
        #添加响应行
        response = "HTTP/1.1 404 not found\r\n"
        response += '\r\n'   #空行
        response += '====网页没找到===='  #相应体
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        for i in f:
            response += i 
    finally:
        connfd.send(response.encode())


#基础配置，功能函数的调用
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8000))
    sockfd.listen(10)
    while True:
        print("Listen to the port 8000.....")
        connfd,addr = sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()


if __name__ == "__main__":
    main()
