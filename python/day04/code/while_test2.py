 # 2、写程序，输入两个整数，第一个用begin绑定，第二个用end变量绑定，打印出begin~end的所有的整数

begin = int(input("请输入开始的整数："))
end = int(input("请输入结束的整数："))

while begin < end+1:
    print(begin)
    begin += 1