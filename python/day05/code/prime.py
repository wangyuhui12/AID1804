
# 练习：
#  输入一个整数n,判断这个整数是否是素数(prime)（素数是指只能被1和自身整除的数）
#  如：
#   2 3 5 7

n = int(input("请输入一个整数："))

# if n <= 1:
#     print("不是素数")
# elif n == 2:
#     print("是素数")
# else:
#     for i in range(2,n):
#         if n%i == 0:
#             print("不是素数")
#             break
#     else:
#         print("是素数")

if n <= 1:
    print(n,"不是素数！")
else:    
    for i in range(2,n):
        if n%i == 0:
            print(n,"不是素数")
            break
    else:
        print(n,"是素数")


# def primes():
#     yield 2
#     i = 3
#     while True:
#         for j in range(2,i):
#             if i%j == 0:
#                 i += 1
#                 break
#         else:
#             yield i
#         i += 1

# if n in primes():
#     print("1")
# else:
#     print("0")