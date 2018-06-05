
g = int(input("请输入学生的成绩(0~100):"))

if g < 0 or g > 100:
    print("成绩不合法！")
else:
    if g > 90:
        print("优")
    elif g > 80:
        print("良")
    elif g >= 60:
        print("及格")
    else:
        print("不及格")1