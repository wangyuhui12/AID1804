

# 此示例示意 assert 语句的使用

def get_age():
    a = int(input("请输入年龄："))
    assert a <= a <= 140, '年龄不在合法的范围内'
    return a

try:
    age = get_age()
except AssertionError as e:
    print("错误原因是：",e)
    age = 0

print(age)