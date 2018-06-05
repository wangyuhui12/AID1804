

# 练习：
# 　１、素数prime函数练习
#     １）写一个函数isprime(x)  判断x是否为素数，如果是素数，返回True，否则返回False
#     2)写一个函数prime_m2n(m, n),返回m 开始到ｎ结束的范围内的素数列表，
#     如：
#         L = prime_m2n(1, 10)
#         print(L)   # [2, 3, 5, 7]
#     3) 写一个函数primes(n), 返回指定范围内素数(不包含n)的全部素数的列表，并打印这些素数
#     如：
#         L = prime(20)
#         print(L)   # [2, 3, 5, 7, 11, 13, 17, 19]
#         １）打印１００以内的全部素数
#         ２）打印１００以内全部素数的和

def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    else:
        return True

def prime_m2n(m, n):
    L = []
    for i in range(m, n):
        if isprime(i) is True:
            L.append(i)
    return L

def primes(n):
    m = 0
    L = prime_m2n(m, n)
    return L

print("100以内的全部素数是：", primes(100))
print("100以内全部素数的和：", sum(primes(100)))