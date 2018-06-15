'''
    tftp 文件服务程序
'''
from socket import * 
import os
import signal
import sys
import time

# 文件库的位置
FILE_PATH = "/home/tarena/"


# 实现服务器功能模块
class TftpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        #　获取列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        files = ""
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files + file + '#'
        self.connfd.send(files.encode())


    def do_get(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'rb')
        except:
            self.connfd.send("文件不存在".encode())
            return
        self.connfd.send("OK".encode())
        time.sleep(0.1)
        #　发送文件
        for line in fd:
            self.connfd.send(line)
        fd.close()
        
        time.sleep(0.1)
        self.connfd.send("##".encode())
        print("文件发送完毕！")


    def do_put(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'w')
        except:
            self.connfd.send("无法完成上传".encode())
        self.connfd.send("OK".encode())
        while True:
            try:
                data = self.connfd.recv(1024).decode()
                if data == '##':
                    break
                fd.write(data)
            except Exception as e:
                print(e)
        fd.close() 
        print("上传完毕")
        


# 作为流程控制， 创建套接字连接， 接受请求
def main():
    HOST = '127.0.0.1'
    PORT = 8888
    ADDR = (HOST, PORT)

    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen to port 8888...")

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        print("客户端登录:", addr)
        # 创建父子进程
        pid = os.fork()
        if pid < 0:
            print("创建进程失败")
            continue
        elif pid == 0:
            sockfd.close()
            tftp = TftpServer(connfd)
            # 接受客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if not data:
                    print("客户端退出")
                    sys.exit(0)
                elif data[0] == 'L':
                    tftp.do_list()
                    # data  --> G filename
                elif data[0] == "G":
                    filename = data.split(' ')[-1]
                    tftp.do_get(filename)
                elif data[0] == "P":
                    filename = data.split(' ')[-1]
                    tftp.do_put(filename)
                elif data[0] == "Q":
                    # 结束子进程
                    print("客户端退出")
                    sys.exit(0)

        else:
            connfd.close()
            continue

if __name__ == "__main__":
    main()


