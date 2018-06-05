
n = int(input("请输入一个月份："))

if n < 1 or n > 12:
    print("您的输入有误！")
else:
    s = n//4
    print("您输入的月份是第",s+1, "季度")