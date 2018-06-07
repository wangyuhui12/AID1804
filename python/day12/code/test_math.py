
# 练习：
# 　１、输入一个正方形的周长，输出正方形的面积
# 　２、输入一个圆的半径，打印出这个圆的面积
# 　３、输入一个正方形的面积，打印这个正方形的周长
# 　（要求：用math模块内的函数和变量）

import math
from math import pi

l = float(input("请输入正方形的周长："))
print("正方形的面积为：",math.pow(l/4, 2))

r = float(input("请输入一个圆的半径："))
print("圆的面积为：", round(pi*r**2, 2))

n = float(input("输入正方形的面积："))
print("正方形的面积为：", math.sqrt(n) * 4)