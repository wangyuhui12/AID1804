
# i = 1

# while i < 20:
#     print("hello world!")
#     i += 1
# else:
#     print("条件不满足，循环结束！")

# 练习：
#  编写程序，用while语句解决下面的问题
#  问题：
#     输入一个数用n绑定，打印出n行的"hello world!"
    
n = int(input("请输入一个整数："))
i = 0

while i < n:
    print("hello world!")
    i += 1

for i in range(n):
    print("hello hi")