
n = int(input("请输入一个整数："))

# def fibs(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         result = fibs(n-1) + fibs(n-2)
#         return result

# L = []
# for i in range(1,10):
#     L.append(fibs(i))

# print(L)


def fibs(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a

L = []
for i in range(n):
    L.append(fibs(i))

print(L)