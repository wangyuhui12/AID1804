
# 练习：
#     1、写一个程序，输入一些单词和解释，将单词作为键，将解释作为值，将这些数据存入字典中
#         然后：
#             输入查询的单词，显示出此单词的解释

d = {}
while True:
    k = input("请输入一个单词：")
    if not k:
        break
    w = input("请输入单词释义：")
    d[k] = w

while True:
    s = input("请输入您要查询的单词：")    

    if s not in d:
        print("单词有误！请重新输入!")
    else:
        break

print('单词释义为：',d[s])


