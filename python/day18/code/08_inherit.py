
# 此示例示意继承和派生
class Human():

    '''此类用来描述人类的共性行为'''
    def __init__(self):
        self.age = 20

    def say(self, that):
        print("说：", that)

    def walk(self, distance):
        print("走了", distance, "公里")

class Student(Human):

    def __init__(self):
        self.score = 90
        super().__init__() # 调用父类同名函数

    def study(self, subject):
        print("正在学习", subject)

    def print(self):
        print(self.age)
        print(self.score)


h1 = Human()
h1.say("今天天气不热！")
h1.walk(5)
h2 = Student()
h2.say("今天天气真热！")
h2.study("历史")
h2.print()  # 20