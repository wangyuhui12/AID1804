
from multiprocessing import Process
import time

class ClockProcess(Process):
    """docstring for ClockProcess"""
    def __init__(self, value):
        #　使用父类的init保证同时拥有父类的属性
        super(ClockProcess, self).__init__()
        #Process.__init__(self)
        self.value = value
        
    # 自定义的类中，重写run方法
    def run(self):
        for i in range(5):
            print("The time is {}".format(time.ctime()))
            time.sleep(self.value)

# 用自己的类创建进程对象
p = ClockProcess(2)

#　会自动执行run 方法
p.start()
p.join()

