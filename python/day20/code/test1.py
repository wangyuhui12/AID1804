

class Fibonacci:

    def __init__(self, max1):
        self.a = 1
        self.b = 1
        self.max = max1

    def __iter__(self):

        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        if fib > self.max:
            raise StopIteration
        return self

it = Fibonacci(100)

for i in it:
    print(i)