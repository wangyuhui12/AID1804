

 # 3、算出100~999以内的水仙花数(Narcissistic number)
 #    水仙花数是指百位的3次方加上十位的3次方加上各位的3次方等于原数的数字
 #    例如：
 #        153 = 1**3 + 5**3 + 3**3

for i in range(100,999):
    s = str(i)
    m = int(s[0])**3+int(s[1])**3+int(s[2])**3
    if m == i:
        print(i,end=' ')
    else:
        continue

print()
