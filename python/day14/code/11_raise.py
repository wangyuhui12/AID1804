
#　此示例示意raise 语句的使用

def make_except():
    def f():
        print("开始...")
        # raise ValueError("invalid value")  # 手动发生一个错误通知
        # try:
        #     n = int(input())
        # except ValueError:
        #     raise ZeroDivisionError("ZeroDivsion")
        e = ZeroDivisionError("被零整除了")
        raise e   # 触发e绑定的错误，进入异常状态
        print("结束...")
    f()
    print("make_except")

try:
    make_except()
except ZeroDivisionError:
    print("raise 已处理")

print("make_except 调用完毕")