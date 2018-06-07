
# ２、　写一个函数myfac来计算n!(n的阶乘)
# 　　n! = 1*2*3*4*..*n
# 如：
#     print(myfac(5))  # 120

def myfac(n):
    mul = 1
    for x in range(1, n+1):
        mul *= x
    return mul

n = int(input("请输入一个整数："))
print(myfac(n))