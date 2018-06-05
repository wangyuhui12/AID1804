
# 练习
#     写程序，输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数：
#         如：
#         输入： ABCDABCABA
#         输出：
#             A ：4次
#         不要求打印顺序

s = input("请输入一段字符串：")

# d = {}
# for i in s:
#     d[i] = None    # 统计i在字符串中出现的个数

# # print(d)
# for k in d:    # d.items()返回字典的键-值对象，将键值直接赋值给k,v
#     print(k,s.count(k),'次')

# L = list(s)
# L1 = []
# for i in L:
#     if i in L1:
#         continue
#     else:
#         L1.append(i)

# for j in L1:
#     print(j,L.count(j),'次')

p = list(set(s))
for i in p:
    print(i,s.count(i),'次')


    
