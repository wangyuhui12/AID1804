
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

#生成协程对象
gr1 = greenlet(test1)
gr2 = greenlet(test2)

#　协程对象调用函数
gr1.switch()

