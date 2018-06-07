


class Student(object):
    def __init__(self):
        self.L = self.input_student()

    def set_L(self, L):
        self.L += L


    def input_student(self):
        L = []
        while True:
            d = {}
            name = input("请输入学生姓名：")
            if not name:
                break
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生分数:"))
            d = [name, age, score]
            L.append(d)
        return L


    def output_student(self):
        print('+','-'*10,'+','-'*10,'+','-'*10,'+')
        # print(('-'*10).join('+'*4))
        print('|','name'.center(10),'|','age'.center(10),'|','score'.center(10),'|')
        print('+','-'*10,'+','-'*10,'+','-'*10,'+')
        # print(('-'*10).join('+'*4))   
    
        for i in self.L:
            print('|',i[0].center(10),'|',
                str(i[1]).center(10),'|',str(i[2]).center(10),'|')
        print('+','-'*10,'+','-'*10,'+','-'*10,'+')
    
    def change_student(self):
        change_name = input("请输入要修改学生的姓名：")
        change_age = int(input("请输入修改学生年龄："))
        change_score = int(input("请输入修改学生分数："))
        for d in self.L:
            if change_name == d[0]:
                d[1] = change_age
                d[2] = change_score
        return self.L
    
    def delete_student(self):
        delete_name = input("请输入要删除的学生姓名：")
        for d in self.L:
            if d[0] == delete_name:
                self.L.remove(d)
        return self.L
    
    def scoreHighToLow(self):
        self.L = sorted(self.L,key=(lambda x: x[2]), reverse=True)
        self.output_student()
    
    def scoreLowToHigh(self):
        self.L = sorted(self.L, key=(lambda x:x[2]))
        self.output_student()
    
    def ageOldToYoung(self):
        self.L = sorted(self.L, key=(lambda x:x[1]), reverse=True)
        self.output_student()
    
    def ageYoungToOld(self):
        self.L = sorted(self.L, key=(lambda x:x[1]))
        self.output_student()
    
    def student_info_save(self):
        with open('si.txt','w') as f:
            for d in self.L:
                age = d[1]
                score = d[2]
                st = d[0] + ','+str(age) + ','+ str(score) +'\n'
                f.write(st)
    
    def student_info_read(self):
        with open('si.txt') as f:
            F = f.read()
            print("学生信息为：")
            print(F)

