from socket import * 

s = socket()
s.connect(('127.0.0.1',8888))

f = open('file_recv.jpg','wb')

while True:
    data = s.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
s.close()