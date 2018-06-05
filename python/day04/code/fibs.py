
# 实现函数fibs(n)得到n个斐波那契数列，列表作为返回值
# 1）通过递归实现
# 2） 通过非递归实现

# 通过递归实现

n = int(input("请输入一个整数:"))

# def fibs(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         result = fibs(n-1) + fibs(n-2)
#         return result

# L = []
# for i in range(1,n+1):
#     L.append(fibs(i))

# print(L)

def fibs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b  # 第n个斐波那契数通过循环求出
    return a   # return 放在循环外部

L = []
for x in range(1,n+1):    # 注意fibs(0)不存在
    L.append(fibs(x))

print(L)

