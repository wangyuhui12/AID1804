
# 练习：
#  写程序，实现如下需求：
#     将如下数据形成一个字典seasons
#         '键'     '值'
#          1        '春季有1,2,3月'
#          2        '春季有4,5,6月'
#          3        '春季有7,8,9月'
#          4        '春季有10,11,12月'         
#     让用户输入一个整数代表这个季度，打印这个季度的信息，如果用户输入的信息不在字典的键内，则打印信息不存在

# n = int(input("请输入季度(1~4)(输入0结束)："))

d = {
    1 : '春季有1,2,3月',
    2 : '春季有4,5,6月',
    3 : '春季有7,8,9月',
    4 : '春季有10,11,12月'
}

while True:
    n = int(input("请输入季度(1~4)(输入0结束)："))
    if n == 0:
        print("程序结束！")
        break
    print(d.get(n,"信息不存在"))


# print(d.get(n,"信息不存在"))

# if n in d:
#     print(d[n])
# else:
#     print("信息不存在")
