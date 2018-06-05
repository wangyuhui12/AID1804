

    # 2 猴子吃桃
    #     有一只小猴子，摘了很多桃子
    #         第１天吃了全部桃子的一半，感觉不饱又吃了一个
    #         第２天吃了剩下的一半，感觉不饱，又吃了一个
    #         ...一次类推
    #         到第１０天，发现只剩一个了
    #     请问第一天摘了多少桃子？

# def myfun(n):
#     if n == 10:
#         return 1
#     else:
#         return (myfun(n+1)+1)*2

# print(myfun(1))



# myfun(n)  表示第n天的桃子数
# n = 10   myfun(10)    1
# myfun(1)   

# myfun(n) = myfun(n-1)/2 - 1
# myfun(n) = (myfun(n+1) +1)*2

a = 1
b = 4
for i in range(9):
    a, b = b, (b+1)*2

print(a)