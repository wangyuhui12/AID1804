


# 练习：
# 　定义一个学生类：
# class Student():
#     def set_info(self, name, age):
#         '''此方法用来给学生添加'姓名'和'年龄'属性'''
#
#     def show_info(self):
#         '''此处显示此学生的信息'''
#
#
# 如：
# 　s1 = Student()
# s1.set_info('小张', 20)
# s2.Student()
# s2.set_info('小李', 18)
# s1.show_info()  # 小张　今年　２０岁
# s2.show_info()  # 小李　今年　　１８岁

class Student(object):

    def set_info(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name,'今年',self.age,sep='')

s1 = Student()
s1.set_info('小张', 20)
s2 = Student()
s2.set_info('小李', 18)
s1.show_info()  # 小张　今年　２０岁
s2.show_info()  # 小李　今年　　１８岁