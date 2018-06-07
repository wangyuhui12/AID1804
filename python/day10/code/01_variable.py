

# a = 100
# b = 200
# def fx(c):
#     d = 400
#     print(a, b, c, d)
#     global a
#     a = 1

# fx(300)
# print('a =', a)

a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    print("locals()返回:", locals())
    print("globals()返回", globals())
    for k, v in globals().items():
        print(k,'--->', v)
    print(c)   # 100
    print(globals()['c'])


fn(100, 200)