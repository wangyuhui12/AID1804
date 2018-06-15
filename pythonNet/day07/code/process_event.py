
from multiprocessing import Event, Process
from time import sleep

def wait_event():
    print("像操作临界区但是要等待临界设置")
    e.wait()
    print("终于轮到我操作临界区了", e.is_set())

def wait_event_timeout():
    print("也想操作临界区但是也要等2秒吧")
    e.wait(2)
    print("2秒到了我不等了", e.is_set())

e = Event()
p1 = Process(target = wait_event)
p2 = Process(target = wait_event_timeout)

p1.start()
p2.start()

print("假装主进程在操作临界资源")
sleep(3)

e.set()
print("开放临界资源")


p1.join()
p2.join()




