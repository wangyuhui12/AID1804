
 # 2、用循环语句生成如下字符串
 #   "ABC....XYZ"
 #   'AaBb....Zz'
 #   提示：
 #    用ord和chr函数结合循环语句实现

for i in range(65,91):
    x = chr(i)
    print(x,end='')
print()

for j in range(26):
    print(chr(j+65),chr(j+97),sep='',end='')
print()