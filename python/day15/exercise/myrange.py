#
# 练习：
# １、用生成器函数primes(begin, end)，生成素数，给出起始值begin和终止值stop,生成此范围内的全部素数，不包含(stop)

def isprimes(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def primes(begin, end):
    for x in range(begin, end):
        if isprimes(x):
            yield x

def print_primes():
    begin = int(input("请输入起始值："))
    end = int(input("请输入终止值："))
    for i in primes(begin, end):
        print(i, end=' ')

if __name__ == '__main__':
    print_primes()