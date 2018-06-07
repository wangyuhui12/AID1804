#
# 练习：
# １、写一个程序，从键盘输入如下信息：
#     姓名　　和　电话号码
#     如：
#     请输入姓名：　xiaozhang
#     请输入电话： 138888888
#     请输入姓名： xiaoli
#     请输入电话： 139999999
#     请输入姓名：　<回车>
#     把从键盘读取的信息存入'phone_book.txt'文件中
#     然后用sublime text 打开并查看写入的内容

def phone_write():
    try:
        f = open('phone_book.txt','w')    # 以全新的方式去写
        while True:
            name = input("请输入姓名：")
            if not name:
                break
            phone = input("请输入电话号码:")
            f.write(name+'\t'+phone+'\n')
        f.close()
    except OSError:
        print("写入文件失败！")


phone_write()

