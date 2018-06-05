
# 练习：
#  输入一个整数用begin绑定，再输入一个整数用end绑定，打印出从begin~end(包含end)的所有偶数（建议用continue语句跳过奇数）

# begin = int(input("请输入一个整数："))
# end = int(input("请输入一个整数："))

# for i in range(begin,end+1):
#     if i%2 == 1:
#         continue 
#     print(i, end =' ')

# print()

s = 0
for i in range(1,101):
    if i%5 != 0 and i%7 != 0 and i%11 != 0:
        s += i
    else:
        continue

print(s)