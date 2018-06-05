
# 练习：
#  1、写程序，输入一个整数n，代表正方形的宽度和高度。
#  打印数字组成的正方形：
#     如输入：5
#  打印：
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#     1 2 3 4 5
#  输入：4
#  打印：
#     1 2 3 4
#     1 2 3 4
#     1 2 3 4
#     1 2 3 4

# 2、

n = int(input("请输入一个整数:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()

for i in range(1,n+1):
    for j in range(i,n+i):
        print(j%10,end = ' ')
    print()

# L = [1,2,3,4,5,6,7,8,9,0]
# for i in range(n):
#     for j in range(i,n+i):
#         if j > 9:
#             j = j%10
#         print(L[j],end=' ')
#     print()