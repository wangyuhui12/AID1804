

# 练习：
#     任意输入一个单词，存入集合中，当输入空字符串时结束输入
#         1) 打印您输入的单词的种类数（去重）
#         2) 每个单词都打印到终端上显示
#         思考：
#             如何让打印的次序和输入的次序一致

# s = set()
# while True:
#     w = input("请输入一个单词：")
#     if not w:
#         break
#     s.add(w)

# for i in s:
#     print(i, end=' ')

# print()

L = []
while True:
    w = input("请输入一个单词：")
    if not w:
        break
    L.append(w)

L2 = []
for i in L:
    if i not in L2:
        print(i)
    L2.append(i)
