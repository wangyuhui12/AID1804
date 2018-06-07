

def show_menu():
    print("1) 魂斗罗")
    print("2) 超级玛丽")
    print("３）坦克大战")

# print("mypack里的menu模块被加载")

lst = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

def print_list(lst):
    i = 0
    for l in lst:
        if isinstance(l, int):
            i += l
        else:
            i += print_list(l)
        if l == 10:
            return i
            raise ValueError('invalid value')
            # return i
    return i


lst = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
try:
    print(print_list(lst))
except ValueError:
    print(print_list(lst))
# finally:
#     print(print_list(lst))