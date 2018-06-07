

def input_student():
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
    return L

def output_student(L):
    print('+','-'*10,'+','-'*10,'+','-'*10,'+')
    # print(('-'*10).join('+'*4))
    print('|','name'.center(10),'|','age'.center(10),'|','score'.center(10),'|')
    print('+','-'*10,'+','-'*10,'+','-'*10,'+')
    # print(('-'*10).join('+'*4))   

    for i in L:
        print('|',i['name'].center(10),'|',\
            str(i['age']).center(10),'|',str(i['score']).center(10),'|')
    print('+','-'*10,'+','-'*10,'+','-'*10,'+')

def change_student(L):
    change_name = input("请输入要修改学生的姓名：")
    change_age = int(input("请输入修改学生年龄："))
    change_score = int(input("请输入修改学生分数："))
    for d in L:
        if change_name == d['name']:
            d['age'] = change_age
            d['score'] = change_score
    return L

def delete_student(L):
    delete_name = input("请输入要删除的学生姓名：")
    for d in L:
        if d['name'] == delete_name:
            L.remove(d)
    return L

def scoreHighToLow(L):
    L = sorted(L,key=(lambda x: x['score']), reverse=True)
    output_student(L)

def scoreLowToHigh(L):
    L = sorted(L, key=(lambda x:x['score']))
    output_student(L)

def ageOldToYoung(L):
    L = sorted(L, key=(lambda x:x['age']), reverse=True)
    output_student(L)

def ageYoungToOld(L):
    L = sorted(L, key=(lambda x:x['age']))
    output_student(L)

def student_info_save(L):
    with open('si.txt','w') as f:
        for d in L:
            age = d['age']
            score = d['score']
            st = d['name'] + ','+str(age) + ','+ str(score) +'\n'
            f.write(st)

def student_info_read():
    with open('si.txt') as f:
        F = f.read()
        print("学生信息为：")
        print(F)

# ３、为学生管理项目添加两个功能：
#     ９）保存所有学生信息到文件(si.txt)
#    １０）从文件中读取数据(si.txt)
#    (建议：以行为单位存储数据，用空格或逗号作为姓名、年龄、成绩的分隔符）