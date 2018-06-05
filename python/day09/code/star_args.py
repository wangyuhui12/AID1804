
# def func(*args):
#     print("参数个数是：", len(args))
#     print('args=', args)

# func(1, 2, 3, 4)
# func("hello", "world", 1, 2, 3)


# 练习：
# 　写一个函数，　mysum,可以传入任意个实参的数字，返回所有实参的和
# def mysum(...):
#     ....
# print(mysum(1, 2, 3, 4))   # 10
# print(mysum(2, 4, 6))   # 12

def mysum(*args):
    return sum(args)

print(mysum(1, 2, 3, 4))