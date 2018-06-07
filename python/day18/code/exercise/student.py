
class Student():
    count = 0  # 此类变量用来记录学生的个数
    docs = []

    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.score = score
        Student.count += 1  # 让对象个数加１

    @classmethod
    def getTotalCount(cls):
        '''此方法用来得到学生对象的个数'''
        return cls.count

    def __del__(self):
        Student.count -= 1

    def get_score(self):
        return self.score




def test():
    L = []
    L.append(Student('xiaozhang',20,100))
    L.append(Student('xiaowang',20,100))
    L.append(Student('xiaoli',20,100))
    print("此时学生对象的个数是：",Student.getTotalCount())

    L.pop(1)
    print(Student.getTotalCount())

    L2 = []
    L2.append(Student('xiaozhao', 18, 99))
    print(Student.getTotalCount())   # 4

if __name__ == '__main__':
    test()