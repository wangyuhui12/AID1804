
    # 2、有一些数存在于列表L中，如：
    # L = [1, 3, 2, 1, 6, 4, ..., 98, 82]
    #    （此数据自己定义）
    # 将列表L中的数存入于另一个列表L2中（要求，重复出现多次的数字只在L2列表中保留一份）

L = []
while True:
    n = input("请输入一个整数：")
    if not n:
        break
    n = int(n)
    L.append(n)

# for i in L:
#     if L.count(i) > 1:
#         j = L.count(i)
#         for x in range(j-1):
#             L.remove(i)

# 判断i是否在L2中，是则添加，否则continue
L2 =[]
for i in L:
    if i in L2:
        continue
    L2.append(i)
    

print(L2)


    