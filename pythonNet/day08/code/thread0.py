
from threading import Thread
from time import sleep

#　全局变量
l = []

def th1():
    global l 
    l.append(100)

def th2():
    sleep(1)
    print(l)

t1 = Thread(target = th1)
t2 = Thread(target = th2)

t1.start()
t2.start()

# sleep(0.5)
l = [10000]


t1.join()
t2.join()