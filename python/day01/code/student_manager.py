
import time 


def menu():
    print("-------------")
    print("+++++++++++++")


docs = []

def add_student():
    try:
        name = input("请输入姓名：")
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        s = student.Student(name, age, score)
        docs.append(s)
    except:
        pass

def _lines():
    print("+---------+")

def _title():
    print("+   姓名　　　+   年龄　　　+   成绩　　　　+")

def show_students():
    _lines()
    _title()
    _lines()
    for x in docs:
        x.infos()
    _lines()
    time.sleep(2)


while True:
    menu()
    s = input("请选择：")
    if 'q' == s:
        break
    elif '１' == s:
        add_student()
    elif '2' == s:
        show_students()
    else:
        print("输入不正确")
