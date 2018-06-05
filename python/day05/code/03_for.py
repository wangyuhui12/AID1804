
 # 1、求100以内有哪些整数与自身加1的乘积再对11求余结果等于8

for i in range(100):
   s = (i*(i+1))%11
   if s == 8:
       print(i, end=' ')

print()