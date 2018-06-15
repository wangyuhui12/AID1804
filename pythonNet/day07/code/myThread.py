
from threading import Thread
from time import ctime, sleep

#　自己的线程类
class MyThread(Thread):
    def __init__(self, target, name="hah",args=(), kwargs={}):
        super().__init__()
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs


    def run(self):
        self.target(*self.args)

def player(song, sec):
    for i in range(2):
        print("飞天娃！%s : %s" %(song, ctime()))
        sleep(sec)



t = MyThread(target = player, args = ("monkey", 5))
t.start()
t.join()