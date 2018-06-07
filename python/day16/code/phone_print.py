
# ２、写一个读取'phone_book.txt'文件的程序，把保存的信息以表格的形式打印出来
#
# +--------+----------+
# | name   |  number  |
# +--------+----------+

def phone_print():
    with open('phone_book.txt') as f:
        print("+---------------+---------------+")
        print("|     name      |     number    |")
        print("+---------------+---------------+")
        while True:
            F = f.readline()
            if not F:
                break
            L = F[:-1].split('\t')
            print('|',L[0].center(15),'|',L[1].center(15),"|",sep='')
            print("+---------------+---------------+")

if __name__ == '__main__':
    phone_print()
