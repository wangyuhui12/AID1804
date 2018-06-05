
s = input("请输入一个字符串：")

print('第一个字符是：',s[0])
print('最后一个字符是：',s[-1])

if len(s)%2 != 0:
    print('中间的字符是：',s[len(s)//2])