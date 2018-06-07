

# 练习：
# 　写一个生成器函数myodd(x) 来生成一系列奇数
# 如：
# 　myodd(10) 可以生成　1, 3, 5, 7, 9

def myodd(n):
    for x in range(1, n, 2):
        yield x

n = int(input("输入"))
for i in myodd(n):
    print(i)