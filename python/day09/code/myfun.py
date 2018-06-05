

def isprimes(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def factor(n):
    L1 = []
    for i in range(2, n+1):
        if n%i == 0 and isprimes(i):
            L1.append(i)
    return L1

def decom_primes(n,L1,L = []):
    for i in L1:
        if n%i == 0:
            L.append(i)
            n = n/i
            return decom_primes(n,L1)
    return L


n = int(input("请输入一个整数："))
L1 = factor(n)
print(decom_primes(n,L1))




