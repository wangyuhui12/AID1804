
# 练习：
# 实现有序集合
# OrderSet
# 类，能实现两个集合的交集　 & 并集　 |, 补集 -, 对称补集　 ^, ==
# ， !=, in / not in 集合操作
# (要求集合内用list存储数据)
# s1 = OrderSet([1, 2, 3, 4])
# s2 = OrderSet([3, 4, 5])
# print(s1 & s2)  # OrderSet([3, 4])
# print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])
# if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4]):
#     print("不相等")
#
# if s2 == OrderSet(3, 4, 5):
#     print("s2 和 OrderSet(3, 4, 5)相等")
#
# if 2 in s1:
#     print("2 in s1")

class OrderSet:

    def __init__(self, lst):
        self.data = list(lst)

    def __repr__(self):
        return 'OrderSet(%r)' % self.data

    def __rand__(self, other):
        return OrderSet(list(set(self.data) & set(other.data)))

s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  # OrderSet([3, 4])
# print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])
# if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4]):
#     print("不相等")
#
# if s2 == OrderSet(3, 4, 5):
#     print("s2 和 OrderSet(3, 4, 5)相等")
#
# if 2 in s1:
#     print("2 in s1")
