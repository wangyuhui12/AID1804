
try:
    f = open('abc.txt')
    F = f.readline()
    print(F)
    print("文件打开成功")

    f.close()
except OSError:
    print("文件打开失败！")