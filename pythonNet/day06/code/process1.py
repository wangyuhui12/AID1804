
from multiprocessing import Process
from time import sleep

def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" %name)
        print("I'm working...")

#　通过args　kwargs进行参数传递
p = Process(name = "Worker",target = worker, args = (2,), kwargs = {'name':"Tom"})
p.start()

# 进程状态
print("is alive:", p.is_alive())
#进程名称
print("Process name:", p.name)
#　进程PID
print("Process PID:", p.pid)


#　４　代表超时时间
p.join(4)
print("++++++++++")
