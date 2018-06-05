
 # 1、任意输入一些整数，
 #    每次输入一个，当输入负数时结束输入，当输入完成后，打印您输入的这些数的和

# sum1 = 0
# while True:
#    n = int(input("请输入一个整数："))
#    sum1 += n
#    if n < 0:
#        break

# print("您输入的所有正整数的和为：",sum1)

# def f1():
#     v = 200
#     def f2():
#         v = 300
#         def f3():
#             nonlocal v
#             v = 400
#         f3()
#         print('f2.v= ',v )
#     f2()
#     print('f1.v=',v)
# f1()

def getfn():
    def print_hello():
        print("hello")
    return print_hello()

fn = getfn()
print(fn)
print_hello()
