


# # def fun(f):
# #     print("开始打印：")
# #     f()
# #     print("结束问候")
# #     return fun

# # @fun
# # def say(x):
# #     print("开始问候")
# #     print("您好",x)

# # say("老魏")

# # 定义一个装饰器函数解决上述问题
# def mydeco(fn):
#     # print("hah")
#     def fx():
#         print("+++++++++++")
#         fn()
#         print("-----------")
#     # print("fn")
#     return fx
#     # print('fn')

# @mydeco
# # myfunc = mydeco(myfunc)
# # 定义函数地方
# def myfunc():
#     print("myfunc被调用")

# myfunc()

# # myfunc = mydeco(myfunc)
# # myfunc()
# # myfunc()
# # @myfunc
# # def f1()
# myfunc()


def sum_list(lst):
    for i in lst:
        if type(i) is not int:
            lst.extend(i)
            lst.remove(i)
            return sum_list(i)
    return sum(lst)

lst = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
print(sum_list(lst))

