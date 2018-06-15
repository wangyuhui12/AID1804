
#　进程cpu
from test import * 
import multiprocessing
import time

jobs = []

t = time.time()

for i in range(10):
    mp = multiprocessing.Process(target = count, args=(1,1))
    mp.start()
    jobs.append(mp)


for i in jobs:
    i.join()
print("Process CPU:", time.time() - t)