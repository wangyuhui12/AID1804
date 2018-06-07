
# 此示例示意用迭代器来访问可迭代对象

#　用for 语句访问可迭代对象L
L = [2, 3, 5, 7]
for x in L:
    print(L)

# 用while循环语句来访问如下列表：
it = iter(L)
while True:
    try:
        x = next(it)
        print(x)	
    except StopIteration:
	break
	
