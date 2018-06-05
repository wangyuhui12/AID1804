
 # 2、计算1+3+5+7+..+99的和
 # 用while和for语句两种方法实现

s = 0
# for i in range(1,100,2):
#     s += i

j = 1
while True:
    if j == 100:
        break
    s += j
    j += 2

print(s)