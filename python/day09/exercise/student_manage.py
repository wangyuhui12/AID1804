

# # 　２、修改之前的学生信息管理程序：
#     编写两个函数用于封装　录入学生信息　和　打印学生信息的功能
#     1)
#     def input_student():
#         ＃ 此函数获取学生信息，并返回学生信息的字典的列表
#         ...
#     ２）
#     def output_student(L):
#         #　以表格形式再打印学生信息
#         ...
#     验证测试：
#         L = input_student()
#         output_student(L)
#         print("再添加几个学生信息")
#         L += input_student()
#         print("添加学生后的学生信息如下：")
#         output_student(L)





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


if __name__ == '__main__':
    L = input_student()
    output_student(L)
    print("再添加几个学生信息")
    L += input_student()
    print("添加学生后的学生信息如下：")
    output_student(L)