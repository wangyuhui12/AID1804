
# 练习２：
# 定一个类，Fibonacci实现迭代协议，此类的对象可以作为可迭代对象生成相应的斐波那契数
# 1
# 1
# 2
# 3
# 5
# 8　..
# class Fibonacci:
#     def __init__(self, n):
#         ...
#
#     ...
#
#
# 实现如下操作：
# for x in Fibonacci(10):
#     print(x)
# L = [x for x in fibonacci(30)]
#
# print(sum(Fibonacci(25)))
# 　需要实现迭代器协议

class Fibonacci:

    def __init__(self, n):
        self.L = []
        self.a = 1
        self.b = 1
        self.n = n

    def __iter__(self):

        return self

#　n 表示为第n个斐波那契数
    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        self.L.append(self.a)
        if len(self.L) - 1 == self.n:
            raise StopIteration
        return fib

#　n表示n 以内的斐波那契数
    # def __next__(self):
    #     fib = self.a
    #     self.a, self.b = self.b, self.a + self.b
    #     if fib > self.max:
    #         raise StopIteration
    #     return self


for x in Fibonacci(10):
    print(x)

L = [x for x in Fibonacci(30)]
print(L)
print(sum(Fibonacci(25)))
print(next(Fibonacci(10)))
# print(Fibonacci(10))

