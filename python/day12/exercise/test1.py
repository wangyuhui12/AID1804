

# 练习：
#     １、写一个程序，以电子时钟格式打印时间：
#         时间格式为：
#             HH:MM:SS
#         时间每隔一秒刷新一次

import time

while True:
    s = time.time()
    d = time.localtime(s)
    # print(d[3],':',d[4],':',d[5])
    print("%2d:%2d:%2d" % d[3:6], end='\r') # \r　光标始终在开头
    time.sleep(1)

