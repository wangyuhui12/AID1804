import os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child Process :",os.getpid())
    print("Child Process over")
    # print("Parent pid:",os.getppid())
    # sleep(2) #等父进程退出
    # print("Parent pid again:",os.getppid())
else:
    sleep(2)
    print("Parent Process")
    while True:
        pass
    # sleep(1) # 等待子进程打印自己的PID
    