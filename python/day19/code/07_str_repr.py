


# 此示例示意一个自定义的数字类型重写　repr　和　str 方法
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print("__str__被调用")
        return "数字：%d" % self.data

    def __repr__(self):
        return 'Mynumber(%d)' % self.data



n1 = MyNumber(100)
print(str(n1))
print(repr(n1))
print(n1)