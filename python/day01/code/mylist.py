

class MyList():
    def __init__(self, a):
        self.data = a.copy()

    def infos(self):
        return "MyList(" + str(self.data) + ")"

    def __str__(self):
        return self.infos()

    def myadd(self, other):
        r = []
        r.extend(self.data)
        if type(other) == int:
            r.append(other)
        elif type(other) == MyList:
            r.extend(other.data)
        else:
            raise ValueError("other不能为其他值")
        return MyList(r)

    def __add__(self, other):
        return self.myadd(other)

    def __mul__(self, rhs):   # right hand side
        # L0 = MyList([])
        # for x in range(rhs):
        #     L0 += MyList(self.data)
        # return L0

        return MyList(self.data * rhs)
L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])

L3 = L1*3
print(L3)

# L4 = 3*L1   # 报错

# L1 = MyList([1, 2, 3])
# L2 = MyList([4, 5, 6])
# L3 = L1.myadd(L2)
# print(L3)
# L4 = L1 + L2
# print(L4)
# L5 = L1 + 1  # L
# print(L5)
# L = [1, 2, 3]
# L1 = MyList(L)
# # L[2] = 3.14
# print(L1.infos())
# print(L1)
# L2 = MyList([4, 5, 6])
# print(L2.infos())

