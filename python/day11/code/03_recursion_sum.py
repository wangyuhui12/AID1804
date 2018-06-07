
# 4、已知有列表：
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst)打印出所有元素print_list(L)  #打印
#     2) 写一个函数sum_list(lst)
#     返回这个列表中所有元素的和
# 注：
#     type(x) 可以返回一个变量的类型
# 如
#     type(20) is int    # True


def print_list(lst, L=[]):
    for i in lst:
        if type(i) is int:
            L.append(i)
            print(i)
        else:
            # L = print_list(i, L)
            print_list(i, L)  # 列表是不可变类型 ，函数为L创建了同一个指针地址
    return L


def sum_list(lst):
    for i in lst:
        if type(i) is not int:
            lst.extend(i)
            lst.remove(i)
            # return print_list(lst)
    return sum(lst)

def sum_list(lst, L=[]):
    for i in lst:
        if type(i) is int:
            L.append(i)
        else:
            L.extend(sum_list(i, L=[]))
    return L

def sum_list(lst):
    s = 0
    for i in lst:
        if type(i) is int:
            s += i
        else:
            s += sum_list(i)
            # s += sum_list(i)
            # s = sum_list(i s)
    return s
# lst = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# L = print_list(lst)
# print(L)
# print("所有元素的和为：", sum(L))
# print(sum_list(lst))

