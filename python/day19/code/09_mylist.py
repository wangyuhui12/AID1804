

# 自定义一个MyList类，与系统内建的类一样，用来保存有先后关系的数据
class MyList:
    '''自定义列表类'''
    def __init__(self, iterator = ()):
        self.data = [x for x in iterator]

    def __repr__(self):
        return "MyList(%r)" % self.data

    # def __iter__(self):
    #     return self.data

    def __abs__(self):
        #　用生成器表达式表示防止占用内存
        return MyList((abs(x) for x in self.data))
        # return (abs(x) for x in self.data)

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return False

myl = MyList([1, -2, 3, -4])
print(myl)
print(abs(myl))
myl2 = MyList(range(10))
print("myl2长度是",len(myl2))
print(bool(myl2))