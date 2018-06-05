#!/usr/bin/python3

# 练习：
#  写一个程序，输入多行文字，当输入空行时结束输入，将原输入的所有字符串存于列表中
#  1、按原来输入的行的顺序反向打印这些行
#  例如：
#    输入：hello world
#    输入：welcome to china
#    输入：I like python
#    输入：<回车>
# 显示

# 2、打印出您一共输入了多少字符？

L=[]
s1 = 0
while True:
    s = input("请输入字符串：")
    s1 += len(s)
    if not s:
        break
    L.append(s)

L.reverse()
for i in L:
    print(i)

# for i in range(len(L)):
#     # s1 += len(L.pop(0))
#     print(L.pop(0))  # 错误pop了两次

print("一共打印了%d个元素。" % s1)