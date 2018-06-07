

#　此示例示意运算符重载与实例方法的相同点和不同点
class MyNumber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    def __add__(self, other):
        return self.data + other.data

    def __sub__(self, other):
        return self.data - other.data



n1 = MyNumber(100)
n2 = MyNumber(200)
n = n1 + n2
print(n)
print(n1 - n2)