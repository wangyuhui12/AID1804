#
# ２、仿制range函数的功能，写一个生成器函数myrange,要求功能与range功能相近，能实现一个，两个，三个参数传参，生成正向的整数

def myrange(begin, end=None, step=1):
    if not end:
        end = begin
        begin = 0
    while begin < end:
        yield begin
        begin += step


for x in myrange(10):
    print(x, end=' ')
print()

for x in myrange(2, 10):
    print(x, end=' ')
print()

for x in myrange(1, 10, 2):
    print(x, end=' ')

























