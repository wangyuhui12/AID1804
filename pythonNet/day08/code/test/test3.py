

#　多线程IO密集型操作
from test import * 
import threading
import time

jobs = []

def io():
    write()
    read()

t = time.time()

for i in range(10):
    th = threading.Thread(target = io())
    th.start()
    jobs.append(th)


for i in jobs:
    i.join()
print("Thread io:", time.time() - t)