

weight = float(input("请输入您的体重："))

height = float(input("请输入您的身高："))

bmi = weight/height**2

if bmi < 18.5:
    print("体重偏轻")
elif 18.5 <= bmi <= 24:
    print("正常范围")
else:
    print("体重过重")