from socket import * 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)

f = open('file.jpg','rb')

while True:
    data = f.read(1024)
    if not data:
        break 
    c.send(data)
f.close()
c.close()
s.close()