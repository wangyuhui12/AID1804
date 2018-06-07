
# 此示例示意为对象添加属性

class Dog(object):
    def kinds(self, kinds):
        self.kinds = kinds

    def color(self, color):
        self.color = color

    @property
    def obj(self):
        print(self.color,'的',self.kinds,sep='')
        return self.color


# 创建一个对象
dog1 = Dog()
dog1.kinds = '京巴'  # 添加属性kinds
dog1.color = '白色'  # 添加属性 color
dog1.color = '黄色'
dog1.obj

dog2 = Dog()
dog2.kinds = '牧羊犬'
dog2.color = '灰色'
print(dog2.obj)