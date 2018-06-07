

# ２、写程序，将文件中numbers.txt中的整数读入到内存中
# ，重新形成数字组成的列表，计算这些数的最大值、最小值和他们的和

def numbers_read_list():
    L = []
    with open('numbers.txt') as f:
        F = f.read()
        F = F.split('\n')
        for i in F[:-1]:
            L.append(int(i))
    return L

def calcul_numbers(L):
    print("最大值为：", max(L))
    print("最小值为：", min(L))
    print("数字和为：", sum(L))

def main():
    L = numbers_read_list()
    calcul_numbers(L)

if __name__ == '__main__':
    main()
