
# s = input("请输入任意字符串:")

# n = s[::-1]

# if s == n:
#     print("是回文！")
# else:
#     print("不是回文！")

def huiwen(s):
    a = len(s)
    n = a//2
    for i in range(n):
        if s[i] != s[a-i-1]:
            return 0
        else:
            return 1

while True:
    s = input("请输入任意字符串：")
    n = huiwen(s)

    if s == '0':
        break

    if n == 0:
        print(s,"不是回文！")
    else:
        print(s,"是回文！")
