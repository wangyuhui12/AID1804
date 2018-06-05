
 # 3、写程序求多项式的和：
 # 1/1 - 1/3 + 1/5 - 1/7 + 1/9 + ... + 1/(2*n-1)
 # n最大取：1000000
 #  1)打印这个和
 #  2）打印这个和乘以4的值？

sum0 = 1
sum1 = 0
sum2 = 0
n = 1

# for i in range(3,1000000,4):
#     sum1 += 1/i    # 有累加， 所以必须先要定义

i = 3
while i < 1000000:
    sum1 += 1/i
    i += 4

# for j in range(5,1000000,4):
#     sum2 += 1/j
j = 5
while j < 1000000:
    sum2 += 1/j
    j += 4

sum0 = sum0+sum2-sum1

x = 4*sum0
print(sum0)
print(x)