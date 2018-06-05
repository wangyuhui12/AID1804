
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   #　初始化两个计数器a, b

    def __iter__(self):
        return self   # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):   # 使生成的类可以用来索引
        a1, a2 = 1, 1
        for x in range(n):
            a1, a2 = a2, a1 + a2
        return a1

f = Fib()
print(f[10])
for n in Fib():
    print(n)