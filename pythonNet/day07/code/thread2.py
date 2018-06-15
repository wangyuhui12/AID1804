
from threading import Thread, currentThread
from time import sleep

#　线程函数一个参数
def fun(sec):
    print("线程属性测试")
    sleep(sec)
    #　获取线程对象getName() 函数得到线程名称
    print("%s 线程结束" %currentThread().getName())

thread = []
for i in range(3):
    t = Thread(name = 'haha' + str(i),\
    target = fun, args=(3,))
    thread.append(t)
    t.start()
    print(t.is_alive())  # 线程状态

thread[1].setName("喷火娃") #　设置线程名称
print(thread[2].name)



for i in thread:
    i.join()


