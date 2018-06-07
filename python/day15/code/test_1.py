
#
# 练习：
# 　写一个程序，读入任意行的文字，当输入空行时结束输入.
# 打印带有行号的输入结果：
# 如：
# 请输入：　hello <回车>
# 请输入：　world <回车>

def mytest():
    str = []
    while True:
        s = input("请输入：")
        if not s:
            return str
        str.append(s)

def print_text():
    str = mytest()
    for k,v in enumerate(str, start=1):
        print("第%d行:" %k,v)

if __name__ == '__main__':
    print_text()