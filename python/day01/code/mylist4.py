
class MyList:
    def __init__(self, a):
        self.data = a.copy()

    def __str__(self):
        return "MyList(" + str(self.data) + ")"

    def __neg__(self):
        ml = MyList(self.data)
        for x in len(ml.data):
            ml.data[i] = -ml.data[i]
        return ml

    def __invert__(self):
        ml = MyList(self.data)
        ml.data.reverse()  # reverse 为列表反转
        return ml

    def __abs__(self):
        temp = self.data.copy()
        for i in range(len(temp)):
            if temp[i] < 0:
                temp[i] = -temp[i]            
        return MyList(temp)

L1 = MyList([1, 2, 3, -2, -4])
L3 = abs(L1)
L2 = ~L1

print(L3)
print("L2", L2)