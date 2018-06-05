
m = float(input("请输入公里数："))

if m < 0:
    print("数据有误！")
else:
    if m <= 3:
        print("费用：", 13, "元")
    elif 3 < m < 15:
        s = 13 + m*(m-3)
        print("费用：",round(s,1),"元")
    else:
        s = 13 + m*(m-3)+3.45*m
        print("费用：",round(s,1), "元")