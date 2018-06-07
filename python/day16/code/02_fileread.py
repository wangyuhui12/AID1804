
#　此示例示意以文本文件方式读取abc.txt中的数据

# 直接调用了f.close()
# with open('abc.txt') as f:
#     print(f.read())


try:
    f = open('abc.txt')
    print("文件打开成功。")
    s = f.readline()
    print(len(s))
    if s != '':
        print("读取成功，文字是：", s)
    else:
        print("文件内已经没有数据可读了。")
    s = f.readline()
    print("第二行数据是：",s)
    f.close()
except OSError:
    print("文件打开失败！")