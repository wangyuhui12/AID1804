
class Fib():
    def __getitem__(self, n):  # 生成可索引的类
        if isinstance(n, int):  # n 是索引，输出前n个fib数
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice): # n 是切片　对fib数进行切割
            start = n.start   # 切割开始值
            stop = n.stop
            if start is None:
                start = 0
            # 生成fib数
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])  # [1, 1, 2, 3, 5]
print(f[:10])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(f[3:10])