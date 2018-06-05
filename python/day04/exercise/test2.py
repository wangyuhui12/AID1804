
 # 2、写程序用while实现打印三角形。
 #    要求输入一个整数表示三角形的宽度和高度，打印出如下的三种三角形
 #    1）
 #       *
 #      **
 #     ***
 #    ****
 #    2)
 #    ****
 #     ***
 #      **
 #       *
 #    3)
 #    ****
 #    ***
 #    **
 #    *

n = int(input("请输入一个整数表示三角形的宽度和高度："))
i = 1

while i < n+1:
    st = '*'*i
    st1 = '%%%ds' %n
    print(st1 % st)
    i += 1

print()
s = n
while s > 0:
    st = '*'*s
    st1 = '%%%ds' % n
    print(st1 % st)
    s -= 1
 
print()
m = n
while m > 0:
    st = '*'*m
    st1 = '%%%ds' % (-n)
    print(st1 % st)
    m -= 1
 
