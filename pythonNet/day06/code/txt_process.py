

# 练习：
# 　使用multiprocessing　创建两个进程，分别复制一个文件
# 的上半部分和下半部分到另一个新的文件中

from multiprocessing import Process
import os

size = os.path.getsize('clock.py')
# 两个进程操作同一个文件流，会产生错乱
# f = open('clock.py', 'rb')


# 读取文件上半部分
def read_upper(filename):
    f = open(filename, 'rb')
    n = size // 2
    fw = open('1.txt', 'wb')

    while True:
        if n < 128:
            data = f.read(n)
            fw.write(data)
            break    
        data = f.read(128)
        fw.write(data)
        n -= 128
    f.close()
    fw.close()

# 复制下半部分
def read_lower(filename):
    f = open(filename, 'rb')
    fw = open('2.txt', 'wb')
    f.seek(size // 2, 0)
    while True:
        data = f.read(128)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()


p1 = Process(target=read_upper, args=('clock.py',))
p2 = Process(target=read_lower, args=('clock.py',))

p1.start()
p2.start()

p1.join()
p2.join()
