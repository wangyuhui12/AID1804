

 # 写一个函数input_student(),output_student()得到学生的姓名、成绩、年龄
 # (可以把以前的input_student函数直接拿过来用)
 # 1) L = input_student()  #输入一些学生信息
 # print("按年龄从大到小排序后")
 # L2 = sorted(L, ..)
 # output_student(L2)
 # print("按成绩从高到低排序后")
 # L3 = sorted(L, ...)
 # output_student(L3)

def input_student():
    L = []
    while True:
        d = {}
        name = input("请输入学生姓名：")
        if not name:
            break
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生分数："))
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L

def output_student(L, n):
    if n == 'age':
        L = sorted(L, key=lambda x :x['age'], reverse=True)
    if n == 'score':
        L = sorted(L, key=lambda x :x['score'], reverse=True)
    print('+','-'*10,'+','-'*10,'+','-'*10,'+')
    # print(('-'*10).join('+'*4))
    print('|','name'.center(10),'|','age'.center(10),'|','score'.center(10),'|')
    print('+','-'*10,'+','-'*10,'+','-'*10,'+')
    # print(('-'*10).join('+'*4))   

    for i in L:
        print('|',i['name'].center(10),'|',\
            str(i['age']).center(10),'|',str(i['score']).center(10),'|')
    print('+','-'*10,'+','-'*10,'+','-'*10,'+')

def main():
    # 按年龄从小到大排序
    L = input_student()
    while True:
    n = input("请输入要排序的选项(age/score):")
    if not n:
        break
    output_student(L, n)


if __name__ == '__main__':
    main()

