
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("daemon 测试")

t = Thread(target = fun)

t.setDaemon(True)
print(t.isDaemon)
t.start()

print("=======主线程结束========")
