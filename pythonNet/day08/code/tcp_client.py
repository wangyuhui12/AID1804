
from socket import *

s = socket()
s.connect(('127.0.0.1', 8888))

while True:
    data = input("发送：")
    if not data:
        print("*********")
        break
    s.send(data.encode())
    print(data.encode())
    msg = s.recv(1024).decode()
    print(msg)
    
s.close()
