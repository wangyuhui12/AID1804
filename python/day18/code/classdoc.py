

# class Car(object):
#     '''此类用来描述车的对象的行为，
#     这是Car类的文档字符串'''
#     def run(self, speed):
#         '''车的run方法'''
#         pass

class Student(object):
    __slots__ = ['name', 'score']
    # 限定类实例有固定的属性
    def __init__(self, name, score):
        self.name = name
        self.score = score


s1 = Student("小张", 58)
print(s1.score)
