

# 5. 实现一个函数mysplit,  可以按给定的字符分割字符串，将分割后的结果存到列表中，
# 分隔符的默认值为1个空格，并将列表作为函数的返回值。（5分）
# 示例：
# L = mysplit(‘name#age’, ‘#’)
#
# #L为[‘name’,’age’]

def mysplit(str, s):
    L = []
    t = ''
    if s not in str:
        print("输入有误！")
        return
    for x in str:
        if x == s:
            L.append(t)
            t = ''
            continue
        if x == str[-1]:
            t += str[-1]
            L.append(t)
        t += x
    return L

str = input("请输入字符串：")
s = input("请输入分隔符：")
print(mysplit(str, s))


