
# 此示例示意try-except　语句的用法

def div_apple(n):
    print('%d个苹果想分给几个人？' % n)
    s = input('请输入人数：')
    try:
        cnt = int(s)  # << = 可能触发ValueError错误异常
        result = n / cnt  # << = 可能触发ZeroDivisionError 错误异常
        print('每个人分了，',result, '个苹果')
    except ZeroDivisionError:
        print("被零除错误！")
#　以下是调用者
# 我用try-except 语句来捕获并处理　ValueError 类型的错误
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print("div_apple 内出现了　ValueError 错误，　已处理")
    # print('错误信息是：')
# except ZeroDivisionError:
#     print("出现被零除的错误，苹果不分了")
else:
    print("此try语句没有发生异常状态")
finally:
    print("我是finally子句，我一定会执行")

print("程序正常退出")
