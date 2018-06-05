

# 练习：
#     １、写一个函数myfun，此函数用来显示两个参数的相关信息
#         函数：
#             def myfun(a, b):
#                 此处自己实现
#         此函数给定两个参数，打印关于两个参数的信息：
#             1)　打印两个参数的最大值
#             2)　打印两个参数的和
#             3) 打印两个参数的乘积
#             4)　打印从a开始到b结束的所有偶数：
#             如：
#                 myfun(5, 10):


class myfun():
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def max1(self):
        m = max(self.a, self.b)
        return m

    def sum1(self):
        m = sum(self.a, self.b)
        return m

    def mul1(self):
        return self.a * self.b

    def even_num(self):
        print(a,'到',b,'所有的偶数是：')
        for i in range(a, b+1):
            if i % 2 == 0:
                print(i, end=' ')

a = int(input("请输入起始整数："))
b = int(input("请输入终止整数："))
s = myfun(a, b)
# print("两个参数的最大值：", s.max1())
# print("两个参数的和：", s.sum1())
print("两个参数的乘积：", s.mul1())
s.even_num()   
