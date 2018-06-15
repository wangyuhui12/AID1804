
#单进程的执行效率
from test import * 
import time

# t = time.time()
# for i in range(10):
#     count(1,1)


#　IO密集型
t = time.time()
for i in range(10):
    write()
    read()
print("Line CPU", time.time() - t)
