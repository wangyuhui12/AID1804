
# while True:
#     s = 0
#     m = input("请输入您的用户名:")
#     if m == 'tarena':
#         while True:
#             n = input("请输入您的密码：")
#             if n == '123456':
#                 s = 1
#                 print("登录成功！")
#                 break
#             else:
#                 print("密码错误！请重新输入！")
#     else:
#         print("用户名有误，请重新输入！")

#     if s == 1:
#         break

# s = input("请输入一个字符串:")

# p = s[::-1]

# if s == p:
#     return True
# else:
#     return False

L1 = [2,3,5]
L2 = [7,11,13]
L = [14,33,65]

for i in L1:
    for j in L2:
        L.append(i*j)

print(L)