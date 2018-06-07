
# 练习：
# １、写一个函数mysum()，要求给出一个数n，求
# 1 + 2 + 3+... + n的和
# 如：
#     print(mysum(100))  #  5050

def mysum(n):
    s = 0
    for i in range(n+1):
        s += i
    return s

print(mysum(100))