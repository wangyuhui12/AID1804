from multiprocessing import Pool
from time import sleep

def worker(msg):
    sleep(2)
    print(msg)

#　创建进程池对象
pool = Pool(processes = 4)
result = []

for i in range(10):
    msg = 'Hello %d'%i
    #　将事件加入到进程池
    pool.apply_async(func=worker, args = (msg,))
    result.append(i)

#　关闭进程池
pool.close()
# 回收进程池
pool.join()