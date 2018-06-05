

    # ３　完全数：
    #     1 + 2 + 3 = 6

def perfect_number(n):
        L = []
        for i in range(1,n):
            if n%i == 0:
                L.append(i)
        if n == sum(L):
            return 1

n = int(input("请输入一个整数:"))
for i in range(10, n, 2):
    s = str(i)
    if s[-1] == 6 or (s[-1] == 8 and s[-2] == 2):
        if perfect_number(i) == 1:
            print(6,i, end=' ')

# print()
