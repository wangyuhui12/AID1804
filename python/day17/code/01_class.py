

# 定义一个类，类名为Dog
class Dog(object):
    pass



dog1 = Dog()  # 创建Dog类的对象
print(id(dog1))
dog2 = Dog() # 创建Dog类的另一个对象
print(id(dog2))


# 类似于如下语句：
int1 = int()
int2 = int()