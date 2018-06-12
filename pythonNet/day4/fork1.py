import os 
from time import sleep 

pid = os.fork()

a = 1

if pid < 0:
    print("Create Process failed")
elif pid == 0:
    #子进程中变量修改不会影响父进程
    print("a = ",a)
    a = 10000
    print("This is Child process")
else:
    sleep(1)
    print("This is parent process")
    print("parent a =",a)