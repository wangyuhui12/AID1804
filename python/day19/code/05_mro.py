

# 此示例示意在多继承中的对象查找顺序问题

class A:
    def m(self):
        print("A.m")

class B(A):
    def m(self):
        print("B.m")
        super().m()

class C(A):
    def m(self):
        print("C.m")
        super().m()

class D(B, C):
    def m(self):
        print("D.m")
        super().m()


d = D()
d.m()   # 调用方法的顺序是什么？
for x in D.__mro__:
    print(x)