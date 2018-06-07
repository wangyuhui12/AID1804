

'''
此模块示意__name__属性的作用
'''

def f1():
    print('f1被调用')


if __name__ == '__main__':
    print("mymod5.py为主模块")
    f1()
else:
    print("mymod5被其他模块调用")