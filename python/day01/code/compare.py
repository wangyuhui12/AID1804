
class Tree:
    def __init__(self,h):  # h代表树干高度
        self.height = h

    def show(self):
        print(" * ")
        print("***")
        print(" * ")
        print(" * ")

    def __lt__(self, rhs):
        return self.height < rhs.height

    def __le__(self, rhs):
        return self.height <= rhs.height

t1 = Tree(5)
t2 = Tree(10)
if t1 < t2:
    print("t2树高")
else:
    print("t1树高")

