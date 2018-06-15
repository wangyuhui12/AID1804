
#io多进程
from test import * 
import multiprocessing
import time

jobs = []

def io():
    write()
    read()

t = time.time()

for i in range(10):
    th = multiprocessing.Process(target = io())
    th.start()
    jobs.append(th)


for i in jobs:
    i.join()
print("Process io:", time.time() - t)