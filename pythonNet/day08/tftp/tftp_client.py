
from socket import * 
import sys
import time


# 实现基本的请求功能
class TftpServer(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L") #　发送请求类型
        #　等待接受服务器端确认
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file, end='　')
            print("－－－－－文件列表展示完毕－－－－－－\n")

        else:
            #　失败的原因由服务器发送过来
            print(data)

    def do_get(self, filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename, 'w')
            while True:
                try:
                    data = self.sockfd.recv(1024).decode()
                    if data == '##':
                        break
                    fd.write(data)
                except Exception as e:
                    print(e)

            fd.close()
            print("%s 下载完成\n" %filename)
        else:
            print(data)

    def do_put(self, filename):
        try:
            fd = open(filename, 'rb')
        except:
            self.sockfd.send("上传文件不存在".encode())
            return
        self.sockfd.send(("P " + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            for line in fd:
                self.sockfd.send(line)
                
            fd.close()
            time.sleep(0.1)
            self.sockfd.send(b'##')
            print("%s 文件上传完毕"%filename)
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q') # 表示退出


# 套接字连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    sockfd = socket()
    sockfd.connect(ADDR)

    tftp = TftpServer(sockfd)  # tftp对象调用请求方法

    while True:
        print("========命令========")
        print("*******list********")
        print("******get file*****")
        print("******put file*****")
        print("********quit*******")
        print("===================")

        cmd = input("请输入命令>>")

        if cmd.strip() == 'list':
            tftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            tftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            tftp.do_put(filename)
        elif cmd.strip() == 'quit':
            tftp.do_quit()
            sockfd.close()
            sys.exit("欢迎使用")
        else:
            print("请输入正确的命令！！！")
            continue

if __name__ == "__main__":
    main()