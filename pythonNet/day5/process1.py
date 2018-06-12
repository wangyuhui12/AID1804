import multiprocessing as mp 
from time import sleep

a = 1

def fun():
    global a 
    a = 1000
    sleep(3)
    print("子进程事件")

#创建进程对象
p = mp.Process(target = fun)

#启动进程 
p.start() 

# sleep(2)
# print("这是父进程")

#回收进程
p.join()
print("a = ",a)