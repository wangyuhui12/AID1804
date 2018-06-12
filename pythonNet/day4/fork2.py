import os 

pid = os.fork()

if pid < 0:
    print("Create Process failed")
elif pid == 0:
    #获取当前进程进程号
    print("子进程ＰＩＤ",os.getpid())
    #获取父进程进程号
    print("parent PID",os.getppid())
else:
    print("父进程ＰＩＤ",os.getpid())
    print("child PID",pid)  #子进程的ＰＩＤ