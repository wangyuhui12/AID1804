
#
# ２、写一个类Bicycle(自行车)类，有run方法，调用时显示骑行里程km
# class Bicycle:
#     def run(self, km):
#         print("自行车骑行了", km, "公里")
#
#
# 再写一个类EBicycle(电动自行车)类，在Bicycle类的基础上添加电池电量volume属性，有两个方法：
# 　１、file_charge(self, vol)　用来充电，　vol为电量
# 　２、run(km) 方法每骑行10km消耗电量1度，同时显示当前电量，则调用Bicycle的run方法骑行
# class EBicycle(Bicycle):
#     ...
#
# b = Bicycle()
# b.run(10)  # 自行车骑行了10公里
# e = EBicycle(5)
# e.run(10)   # 电动车骑行了１０公里
# e.run(100)　＃电动车骑行了４０公里，自行侧骑行了６０公里
# b.fill_charge(10)
# b.run(100)

class Bicycle(object):

    def run(self, km):
        print("自行车骑行了", km, "公里")


class EBicycle(Bicycle):
    def __init__(self, vol):
        self.vol = vol

    def run(self, km):
        if km <= 10*self.vol:
            print("电动车骑行了", km, "公里")
            self.vol -= km/10
        else:
            print(self.vol)
            print("电动车骑行了", 10*self.vol, end = ' ')
            super().run(km - 10*self.vol)
            self.vol = 0

    def fill_charge(self, vol):
        self.vol += vol



b = Bicycle()
b.run(10)  # 自行车骑行了10公里
e = EBicycle(5)
e.run(10)   # 电动车骑行了１０公里
e.run(100) # 电动车骑行了４０公里，自行侧骑行了６０公里
e.fill_charge(10)
e.run(100)