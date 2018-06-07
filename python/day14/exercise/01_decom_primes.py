

# ２、分解质因数，输入一个正整数，分解质因数：
# 如：
# 　　输入：９０
# 　　　　　则打印：
# 　　90 = 2*3*3*5
# (质因数是指最小能被原数整除的素数(不包括１))

def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n 

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        it = filter(lambda x : x/n > 0, it)

def decom_primes(n, L = []):
    for i in primes():
        if n%i == 0:
            L.append(i)
            n = n/i
            return decom_primes(n)
    return L

n = int(input("请输入一个整数："))
print(n,'=',end=' ')
st = str(i for i in decom_primes(n))
print('*'.join(st))

