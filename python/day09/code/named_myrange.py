
# 练习：
# 　写一个myrange函数，此函数返回一个符合range规则的整数列表
# 　如：
#     L = myrange(3)
#     print(L)
#     L = myrange(3, 6)
#     print(L) # L = [3, 4, 5]
#     L = myrange(1, 10, 3)
#     print(L)

# def myrange(a, b=0, c=1):
#     L = []
#     if b == 0:
#         i = 0
#         while i < a:
#             L.append(i)
#             i += 1
#     while a < b:
#         L.append(a)
#         a += c
#     return L

def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    L = []
    while start < stop:
        L.append(start)
        start += step
    return L

if __name__ == '__main__':
    print(myrange(3))
    print(myrange(3,6))
    print(myrange(1, 10, 3))
