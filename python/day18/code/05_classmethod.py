

class Car():
    count = 0  # 类变量

    @classmethod
    def getTotalCount(cls):
        '''此方法为类方法，第一个参数为cls,代表调用此方法的类'''
        return cls.count

    @classmethod
    def updateCount(cls,number):
        cls.count += number
print(Car.getTotalCount())  # 用类来调用类方法
Car.count += 1   #　面向对象思想不提倡直接操作属性
# Car.updateCount(1)

print(Car.getTotalCount()) #

c1 = Car()
c1.updateCount(100)  # Car　类的实例也可以调用类方法
print(c1.getTotalCount()) # 101

