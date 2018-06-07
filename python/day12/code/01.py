
# def mysum(fn):
#     def fx(lst, L=[]):
#         s1 = fn(lst, L=[])
#         # s1 += sum(s1)
#         print(s1)
#         return s1
#         # print(s1) #s1
#     return fx


# @mysum
# def print_list(lst, L=[]):
#     for i in lst:
#         if type(i) is int:
#             L.append(i)
#             # print(i)
#         else:
#            print_list(i)
#             # print_list(i, L)  # 列表是不可变类型 ，函数为L创建了同一个指针地址
#     return L

# lst = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# print(sum(print_list(lst)))
# # print(print_list(lst))
# print()
# print_list(lst) 
# L = print_list(lst)
# print(L)
# for i in L:
#     print(i)
# L = [1, 2, 3]
# def f(n, lst=[]):
#     lst.append(n)
#     print(lst)

# f(4, L)
# f(5, L)
# f(100)
# f(200)

def print_list(lst):
    L =[]
    for i in lst:
        if type(i) is int:
            L.append(i)
            print(i)
        else:
            # L = print_list(i, L)
            L += print_list(i)  # 列表是不可变类型 ，函数为L创建了同一个指针地址
    return L

lst = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
L = print_list(lst)
print(L)