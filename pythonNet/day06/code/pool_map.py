
from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    print("执行 pool map 事件", n)
    return n * n

pool = Pool(4)
#map放入６个事件到进程池
r = pool.map(fun, range(6))

print("返回值列表：", r)
pool.close()
pool.join()
