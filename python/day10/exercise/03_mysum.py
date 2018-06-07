

# ３、写一个函数，求
#     1 + 2**3 + 3**3 +  ...+n**n的和

def mysum(n):
    s = 0
    for x in range(1, n+1):
        s += x**x

    return s

n = int(input("请输入一个整数："))
print(mysum(n))