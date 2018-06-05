

# 练习：
# 　１、写一个函数　mysum(), 可以传入两个实参或三个实参。如果传入两个实参，则返回两个实参的和
# 　２、如果传入三个实参，则返回前两个实参对实参的和对第三个实参求余的结果

# print(mysum(1, 100))   101
# print(mysum(2, 10, 7))   # 5返回(2+10)%5

def mysum(a, b, c=None):
    # s = (a+b)%c
    # if c == 1:
    #     return a+b
    # else:
    #     return s
    if c is None:
        return a+b
    return (a + b)%c

print(mysum(1, 100))
print(mysum(2, 10, 7))