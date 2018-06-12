
from multiprocessing import Process, Pipe
import os, time

# 创建管道
fd1, fd2 = Pipe(duplex=False)

def fun(name):
    time.sleep(3)
    #向管道内写入内容
    fd2.send("hello" + str(name))

process = []
for i in range(5):
    p = Process(target = fun, args=(i,))
    process.append(p)
    p.start()

for i in range(5):
    #　读取管道消息
    data = fd1.recv()
    print(data)

for i in process:
    i.join()




