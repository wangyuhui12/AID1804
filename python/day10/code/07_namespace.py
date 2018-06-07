

# v = 100   # 全局作用域
# def fun1():
#     v = 200 #　外部嵌套函数的作用域
#     print('fun1内的v=', v)
#     def fun2():
#         v = 300   # 局部作用域
#         print("fun2内的v=", v)
#     fun2()

# fun1()

# print('v=', v)

var = 100
def f1():
    var = 200
    print("f1里的var=", var)
    def f2():
        # nonlocal var
        var = 300  # 此处要想修改f1里的var变量怎么办？
        print("f2里的var=", var)
    f2()
    print("f2调用结束后的var值为", var)
f1()
print("全局的var=", var)