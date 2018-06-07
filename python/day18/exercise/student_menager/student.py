
# 练习
#   1. 用类来描述一个学生的信息(可以修改之前的写的Student类)
#     class Student:
#           # 此处自己实现

#     要求该类的对象用于存储学生信息:
#          姓名,年龄,成绩
#     将这些对象存于列表中.可以任意添加和删除学生信息
#        1. 打印出学生的个数
#        2. 打印出所有学生的平均成绩
#     (建议用类变量存储学生的个数,也可以把列表当作类变量)
class Student(object):

    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score

    def get_infos(self):
        return (self.name, self.age, self.score)

    def is_name(self, name):
        if self.name == name:
            return True
        return False

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("不合法的成绩：" + str(score))
        self.score = score

    def write_to_file(self, file):
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')
