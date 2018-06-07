

# 练习：
# 　写一个计算器解释执行器：
# 有如下函数：
# def myadd(x, y): #　计算两个数相加
#     return x+y
# def mymul(x, y):
#     return x * y
# def get_op(s):  # s 代表操作字符串　：　'加', '乘'
#     pass

# 主函数：
# def main():
#     while True:
#         s = input('请输入计算公式：')
#         L = s.split()
#         a, s, b = L
#         fn = get_op(s)
#         print('结果是：', fn(a, b))  ＃结果是３０


def myadd(x, y):
    return x + y

def mymul(x, y):
    return x * y

def get_op(s):
    if s == '加' or s == '+':
        return myadd
    elif s == '乘' or s == '*':
        return mymul

def main():
    while True:
        s = input("请输入计算公式：")
        if not s:
            break
        L = s.split()  # 默认空格分割
        a, s, b = L
        a, b = int(a), int(b)
        fn = get_op(s)
        print('结果是：', fn(a, b))

main()