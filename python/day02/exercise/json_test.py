
import json

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(std):
        return {
        'name':std.name,
        'age':std.age,
        'score':std.score
        }

s = Student("Bob", 20, 88)
# 报错，Student对象不是一个可序列化为json的对象
# print(json.dump(s))
print(json.dumps(s, default = s.student2dict))
