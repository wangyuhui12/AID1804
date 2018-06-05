
class MyNumber:
    "此类用于定义一个整型数字类，用于演示str函数重载"
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        print("__repr__被调用")
        return "MyNumber(" + repr(self.data)+")"

    def __str__(self):
        print("__str__调用")
        return "整数值(" + str(self.data) + ")"

    def __add__(self, other):
        n = self.data + other.data
        return MyNumber(n)

n1 = MyNumber(100)
n2 = MyNumber(200)
# print(repr(n1))
# print(str(n2))
# print(n2)   # 等同于print(str(n2))
# print(n1, [1,2,3],2j)

print(n1.__add__.(n2))   # 等同于下一行
print(n1 + n2)