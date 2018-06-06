
from socket import * 

#创建套接字
s = socket(AF_INET, SOCK_DGRAM)

#设置可以接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


#固定端口号
s.bind(('', 8888))


while True:
    try:
        msg, addr = s.recvfrom(1024)
        print("从{}获取信息：{}".format(addr, msg.decode()))

    except (KeyboardInterrupt, SyntaxError):
        raise

    except Exception as e:
        print(e)

s.close()


