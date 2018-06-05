
n = int(input("请输入一个年份："))

if n%400 == 0:
    print("闰年")
elif n%100 == 0:
    print("平年")
elif n%4 == 0:
    print("闰年")
else:
    print("平年")