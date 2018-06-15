
import threading
from time import sleep
import os

#　线程函数
def music():
    while True:
        print("0 1"*50)


#　创建线程对象
t = threading.Thread(target = music)
t.start()


while True:
    print("1 0"*50)

t.join()