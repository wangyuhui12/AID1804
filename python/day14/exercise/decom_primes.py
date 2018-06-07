
# ２、分解质因数，输入一个正整数，分解质因数：
# 如：
# 　　输入：９０
# 　　　　　则打印：
# 　　90 = 2*3*3*5
# (质因数是指最小能被原数整除的素数(不包括１))

def isprimes(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % 2 == 0:
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
        if n == 1:
            L.append(i)
            n = n/i 
            return decom_primes(n,L1)
    return L

    




# def primes():
#     L = []
#     s = 1
#     while True:
#         if isprimes(s):
#             L.append(s)
#         s += 1
#         if s > 1000:
#             return L

       
# def decom_primes(n, L =[]):
#     for i in primes():
#         if n % i == 0:
#             L.append(i)
#             n = n / i
#             return decom_primes(n)
#     return L 



def print_list():
    n = int(input("请输入一个整数："))
    L1 = factor(n)
    L = decom_primes(n,L1)
    # print(n,'=', end=' ')
    # for i in range(len(L)-1):
    #     print(L[i],'*',end=' ')
    # print(L[-1])
    s = str(L)[1:-1]
    print(n,'=',s.replace(',','*'))


    # st = ''
    # for i in L:
    #     st += str(i)
    # print(n,'=','*'.join(st))

print_list()



# print(decom_primes(n))