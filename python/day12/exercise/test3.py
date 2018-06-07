

    # ３、请编写函数fun，其功能是计算下列多项式的和
    # sn = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
    # 计算n为100时的值
    # 看一下求出来的和是什么？建议用math.factorial

from math import factorial as fac

# def fun(n):
#     s = 1
#     for i in range(1,n+1):
#         s += 1/(fac(i))

#     return s
def fun(n):
    return sum(
        map(
            (lambda x: 1/(fac(x))),
                range(101)
                ))

n = int(input("请输入求多项式的整数："))
print("多项式的和为：", fun(n))