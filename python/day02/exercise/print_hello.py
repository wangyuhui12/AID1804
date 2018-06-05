
# 　２、输入三行文字，让这三行文字在一个方框居中显示
# 如输入（不要输入中文）
# hello tarena!
# my name is weimingze
# python
# 显示如下：
# +------------------------+
# |     hello tarena       |
# |  my name is weimingze  |
# |        python          |
# +------------------------+

a = input("请输入一个字符串：")
b = input("请输入一个字符串：")
c = input("请输入一个字符串：")

str_long = max(len(a), len(b), len(c))

print('+','-'*str_long,'+')
print('|',a.center(str_long),'|')
print('|',b.center(str_long),'|')
print('|',c.center(str_long),'|')
print('+','-'*str_long,'+')
