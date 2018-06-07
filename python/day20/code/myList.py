

class MyList:

    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, other):
        return MyList(self.data + other.data)


    def __mul__(self, other):
        return 'MyList(%r)' % (self.data * other)



L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
# print(L1)
L3 = L1 + L2
print(L3)
L4 = L2 + L1
print(L4)
L5 = L1 * 2
print(L5)
# print(2*L1)