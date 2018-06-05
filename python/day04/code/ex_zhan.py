
a = input("请输入一行文字：")
b = input("请输入一行文字：")
c = input("请输入一行文字：")

# print("%20s" % a)
# print("%20s" % b)
# print("%20s" % c)

n = max(len(a),len(b),len(c))

fmt = '%%%ds' % n   # '%ns'
print('fmt=',fmt)
print(fmt % a)
print(fmt % b)
print(fmt % c)