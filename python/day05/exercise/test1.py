
 # 1、输入一个整数，代表树干的高度
 #    打印一棵”圣诞树“
 #    打印
 #        *
 #       ***
 #        *
 #        *
 #    输入3
 #        *
 #       ***
 #      *****
 #        *
 #        *
 #        *

n = int(input("请输入一个整数："))
s = 2*n -1

for i in range(1,n+1):
   p = '*'*(2*i-1)
   print(p.center(s))
for j in range(n):
    print('*'.center(s))