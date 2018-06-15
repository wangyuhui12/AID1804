

# ２、司机和售票员的故事
# 　* 创建父子进程分别表示司机和售票员
# 　* 当售票员捕捉到SIGINT信号，　给司机发送SIGUSER1信号，
# 此时司机打印“老司机开车了”
# 　* 当售票员捕捉到SIGQUIT信号，　给司机发送SIGUSER2信号，
# 此时司机打印：“车速有点快，系好安全带”
# 　* 当司机捕捉到SIGTSTP信号，给售票员发送SIGUSER1,此时售票员打印"到站了，请下车"
# 　* 到站后，　售票员先下车（子进程先退出），　然后司机下车

from multiprocessing import Pipe,Process
from time import sleep
from signal import * 
import sys
import os

def handle1(sig, frame):
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(), SIGUSR2)
    elif sig == SIGUSR1:
        print("到站了，请下车")
        os._exit(0)


#　子进程表示售票员
def do_child():
    signal(SIGINT, handle1)
    signal(SIGQUIT,handle1)
    signal(SIGUSR1,handle1)
    signal(SIGTSTP, SIG_IGN)
    while True:
        sleep(2)
        print("车技不错~")


p = Process(target = do_child)
p.start()


def handle2(sig, frame):
    if sig == SIGTSTP:
        os.kill(p.pid, SIGUSR1)
        sleep(1)
        print("司机下车了")
        os._exit(0)
    elif sig == SIGUSR1:
        print("老司机开车了")
    elif sig == SIGUSR2:
        print("车速有点快，系好安全带")
# 父进程表示司机

signal(SIGTSTP,handle2)
signal(SIGUSR1,handle2)
signal(SIGUSR2,handle2)
signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)
while True:
    sleep(2)
    print("dudududu....")
#     print(p.pid)
#     if not p.is_alive():
#         break
p.join()
# print("司机下车了")

