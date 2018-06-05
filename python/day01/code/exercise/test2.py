
a = int(input("请输入学生成绩："))
b = int(input("请输入学生成绩："))
c = int(input("请输入学生成绩："))

max = a if a > b else b 
max = max if max > c else c

min = a if a < c else c
min = min if min < b else b

print("最高分：", max, "最低分：", min)