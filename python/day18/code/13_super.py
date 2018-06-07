

class Human(object):

    a = 1
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def infos(self):
        print("姓名：", self.name)
        print("年龄：", self.age)

class Student(Human):

    # 传参注意
    def __init__(self,n, a, s):
        self.score = s
        super().__init__(n, a)


    def info(self):
        super().infos()
        print(self.score)

    @staticmethod
    def f1():
        a = 1
        return a

    def f2(self):
        b = self.f1()



h1 = Student('xiao',34,78)
print(h1.__class__.a)
h1.info()
print(Student.__bases__)

# h1 = Human('小赵', 20)
# print(h1.__class__)