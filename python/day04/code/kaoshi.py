
class Human():
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def gettel(self):
        return self.tel

m = Human('Tom', 45, '12333333')
print(m.getname())
print(m.getage())