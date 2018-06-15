
from multiprocessing import Process, Lock
import sys
from time import sleep

# sys.stdout标准输出流作为所有进程的临界资源
def writer1():
    # 上锁
    lock.acquire()
    for i in range(5):
        sleep(1)
        sys.stdout.write("writer1输出\n")
    lock.release() # 解锁

def writer2():
    with lock:
        for i in range(5):
            sleep(1)
            sys.stdout.write("writer2输出\n")


# 创建锁
lock = Lock()

w1 = Process(target = writer1)
w2 = Process(target = writer2)

w1.start()
w2.start()

w1.join()
w2.join()
