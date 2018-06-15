
import threading
from time import sleep

msg = None

# 创建事情对象
e = threading.Event()

def bar():
    print("呼叫 foo")
    global msg
    msg = "天王盖地虎"

def foo():
    print("等待口令：")
    sleep(2)
    if msg == "天王盖地虎":
        print("宝塔镇河妖，友军友军，哈哈哈")
    else:
        print("口令错误，biu!biu!biu~ 你死了")
    e.set()


def fun():
    print("呵呵...我是特务我最帅")
    sleep(1)
    # 阻塞，e.set()之后才能执行
    e.wait()
    global msg
    msg = "山重水复疑无路"


t1 = threading.Thread(target = bar)
t2 = threading.Thread(target = foo)
t3 = threading.Thread(target = fun)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
