
import gevent

def foo():
    print("Running in foo")
    gevent.sleep(2)
    print("switch to foo again")

def bar():
    print("Running in bar")
    gevent.sleep(3)
    print("switch to bar again")

# 将两个函数设置为协程，此时协程函数运行
f = gevent.spawn(foo)
b = gevent.spawn(bar)

# 回收协程
gevent.joinall([f, b])

