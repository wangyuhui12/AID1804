import os
from time import sleep 

# fork之前的代码只有父进程会执行
print("*******************")
#fork之前产生内存空间的存储，子进程也会有
a = 1
#创建新的进程
pid = os.fork()

if pid < 0:
    print("创建进程失败")
# 只有子进程执行的部分
elif pid == 0:
    sleep(1)
    print("a = ",a)
    print("新创建的进程")
# 只有父进程会运行的部分
else:
    sleep(5)
    print("原来的进程")

#if结构外的代码父子进程都会执行
print("程序执行完毕")