
# 4、修改之前的学生信息管理程序，实现添加菜单和选择菜单操作功能：
# 菜单：
#     +----------------------------+
#     |  1)添加学生信息             |
#     |  2）查看所有学生信息        |
#     |  3) 修改学生的成绩         |
#     |  4) 删除学生信息           |
#     |  q) 退出                  |
#     +---------------------------+
#     请选择：1
#         请输入姓名：...
#     请选择：3
#         请输入修改学生的姓名：...
#     (要求每个功能都对应一个函数)



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

def menu():
    print("+----------------------------+")
    print("|  1) 添加学生信息           |")
    print("|  2) 查看所有学生信息       |")
    print("|  3) 修改学生的成绩         |")
    print("|  4) 删除学生信息           |")
    print("|  q) 退出                   |")
    print("+----------------------------+")

def main():
    L = []
    while True:
        menu()
        s = input("请选择：")
        if s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            change_student(L)
        elif s == '4':
            delete_student(L)
        else:
            break

            
if __name__ == '__main__':
    main()