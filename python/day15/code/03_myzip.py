
# 此示例示意zip函数的内部实行机制

def myzip(iter1, iter2):
    iter1 = iter(iter1)
    iter2 = iter(iter2)
    while True:
        x = next(iter1)
        y = next(iter2)
        yield (x, y)


numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
# for 语句遇到 StopIteration 停止取值
for n, a in myzip(numbers, names):
    print(a, '的客服号码是：', n)