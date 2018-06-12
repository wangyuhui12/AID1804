import os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    sleep(3)
    print("Child process over")
    os._exit(2)
else:
    # 等子进程执行完毕
    pid,status = os.wait()
    print("++++++++++++++++++++")
    print(pid,status)
    print(os.WEXITSTATUS(status)) #获取退出状态
    while True:
        pass
