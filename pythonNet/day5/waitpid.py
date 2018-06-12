# watipid.py
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
    while True:
        sleep(1)
        # 设置非阻塞状态
        pid,status = os.waitpid(-1,os.WNOHANG)
        print("++++++++++++++++++++")
        print(pid,status)
        print(os.WEXITSTATUS(status)) #获取退出状态
    while True:
        pass
