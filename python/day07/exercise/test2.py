
    # 2、学生管理项目准备工作：
    #     写一个程序，任意输入n个学生的信息，形成字典后存于列表中：
    #         学生信息包括：
    #             姓名(字符串)
    #             年龄(整数)
    #             成绩(整数)
    #         循环输入学生信息，直到输入学生姓名为空时结束输入
    #     最后形成字典列表如下：
    #         L = [
    #         {'name': 'xiaozhang', 'age':20, 'score':100}
    #         {'name': 'xiaoli', 'age':21, 'score':98}
    #         {'name': 'xiaowang', 'age':19, 'score':89}            
    #         ]
    #    +------- +--------+------+
    #    |  name  |  age   | score|
    #    +--------+--------+------+

L = []
while True:
    d = {}
    name = input("请输入学生姓名：")
    if not name:
        break
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生分数:"))
    d['name'] = name
    d['age'] = age
    d['score'] = score
    L.append(d)

# L = [{'score': 90, 'name': 'tom', 'age': 20},
#  {'score': 98, 'name': 'lisa', 'age': 23},
#   {'score': 99, 'name': 'jerry', 'age': 21}]

print('+','-'*10,'+','-'*10,'+','-'*10,'+')
# print(('-'*10).join('+'*4))
print('|','name'.center(10),'|','age'.center(10),'|','score'.center(10),'|')
print('+','-'*10,'+','-'*10,'+','-'*10,'+')
# print(('-'*10).join('+'*4))

for i in L:
    print('|',i['name'].center(10),'|',\
        str(i['age']).center(10),'|',str(i['score']).center(10),'|')
print('+','-'*10,'+','-'*10,'+','-'*10,'+')
