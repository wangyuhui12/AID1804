
    # 3、生成前40个斐波那契数（Fibonacci）
    #  1 1 2 3 5 8 
    #  要求：将这些数保存在列表中，最后打印列表中的这些数

# def fibs(n):
#     L = [1,1]
#     a, b = 1, 2
#     for i in range(2,n):
#         a, b = b, a+b
#         L.append(a)
#     return L

# n = int(input("请输入一个整数："))
# print(fibs(n))

n = int(input("请输入一个整数："))

a, b = 0, 1
L = []
for i in range(n):
    a, b = b, a+b
    L.append(a)

print(L)