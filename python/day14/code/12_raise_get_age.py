
# 此示例示意用　raise 发出错误通知给调用者

# 甲写了函数 get_age 

def get_age():
    a = int(input("请输入年龄(0~140):"))
    # if a < 0 or a > 140:
    #     raise ValueError('invalid value')
    if a > 140:
        raise OverflowError("年龄不可能大于140")
    if a < 0:
        raise 
    return a


try:
    age = get_age()
except ValueError:
    print("输入不合法！")
    age = 0
print("得到的年龄是：", age)