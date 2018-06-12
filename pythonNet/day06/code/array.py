
from multiprocessing import Process, Array
import time

# #　创建共享内存
# shm = Array('i', [1, 2, 3, 4, 5])

#　表示在共享内存中开辟5个整型空间
shm = Array('i', 5)

def fun():
    for i in shm:
        print(i)
    #　修改共享内存的内容
    shm[3] = 1000

p = Process(target = fun)
p.start()
p.join()
for i in shm:
    print(i)