
from multiprocessing import Process, Value
import time
import random

money = Value('i', 2000)

#存钱进程
def deposite():
    for i in range(100):
        time.sleep(0.05)
        #对value属性操作实际就是在操作共享内存
        money.value += random.randint(1, 200)

#　取钱
def withdraw():
    for i in range(100):
        time.sleep(0.04)
        #对value属性操作实际就是在操作共享内存
        money.value -= random.randint(1, 200)

d = Process(target = deposite)
w = Process(target = withdraw)

d.start()
w.start()

d.join()
w.join()
print(money.value)