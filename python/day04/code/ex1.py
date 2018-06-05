

while True:
    s = input("请输入一个字符串（输入０结束）：")
    a = s.count(' ')
    print("您输入的字符串中有%d个空格。"%a)
    s1 = s.strip()
    print("有效字符的长度:",len(s1))
    if s.isdigit():
        print("您输入的字符串是数字。")
    if s == '0':
        break           