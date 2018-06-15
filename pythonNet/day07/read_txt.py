
from multiprocessing import Process
import os

size = os.path.getsize('day07.txt')

def read_txt(filename):
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

def read_lower(filename):
    f = open(filename, 'rb')
    fw = open('2.txt', 'wb')
    f.seek(size//2, 0)

    while True:
        data = f.read(128)
        if not data:
            print(data)
            # fw.write(data)
            break
        fw.write(data)

p1 = Process(target=read_txt, args=('day07.txt',))
p2 = Process(target=read_lower, args=('day07.txt',))

p1.start()
p2.start()
p1.join()
p2.join()