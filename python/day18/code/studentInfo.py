
# 练习：
#  １、用类来描述一个学生的信息（可以用修改之前写的Student类）
#  class Student():
#     #　此处自己实现
#    要求该类的对象用于存储学生信息：
#     姓名、年龄、成绩
#    将这些对象存于列表中，可以任意添加和删除学生信息
#     １、打印出学生的个数
#     ２、打印出所有学生的平均成绩
#     （建议用类变量存储学生的个数，也可以把列表当做类变量）

class Student(object):

    def __init__(self):
        self.L = self.input_stdudent_info()


    def input_stdudent_info(self):
        L = []
        while True:
            name = input("请输入学生姓名：")
            if not name:
                break
            age = int(input("请输入学生年龄:"))
            score = int(input("请输入学生分数："))
            L.append((name, age, score))
        return L

    def print_student_info(self):
        print(self.L)
        print("学生个数为：",len(self.L))

    def student_number(self):
        list = []
        for r in self.L:
            list.append(r[-1])
        print("平均成绩为：", sum(list)/(len(self.L)))

    def delete_student_info(self):
        name = input("请输入删除学生信息的名字：")
        lst = []
        for t in self.L:
            if t[0] == name:
                continue
            lst.append(t)
        self.L = lst
        self.print_student_info()

    def append_student_info(self):
        lst = self.input_stdudent_info()
        self.L += lst
        self.print_student_info()






s = Student()
s.input_stdudent_info()
s.print_student_info()
s.student_number()

s.delete_student_info()
s.append_student_info()

