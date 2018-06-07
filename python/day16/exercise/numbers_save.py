

# 练习：
# １、写程序让用户输入一系列整数，当输入小于0的数时结束输入。
#     １）将输入的数字存于列表当中
#     ２）将列表中的数字写入到文件numbers.txt中
#     　（提示：需要将整数转为字符串或字节穿才能存入文件中）

def numbers_list():
    L = []
    while True:
        number = int(input("请输入整数："))
        if number < 0:
            return L
        L.append(number)

def numbers_save(L):
    with open('numbers.txt','w') as f:
        for i in L:
            f.write(str(i)+'\n')

def main():
    L = numbers_list()
    numbers_save(L)

if __name__ == '__main__':
    main()