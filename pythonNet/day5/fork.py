#创建二级子进程处理僵尸

import os  
from time import sleep

def fun1():
    sleep(3)
    print("第一件事情")

def fun2():
    sleep(4)
    print("第二件事情")

pid = os.fork()

if pid < 0:
    print("create process error")
elif pid == 0:
    #创建二级子进程
    pid0 = os.fork()
    if pid0 < 0:
        print("create pid0 failed")
    elif pid0 == 0:
        fun2()  #做另一件事情
    else:
        os._exit(0)
else:
    os.wait()
    fun1()  #做第一件事情