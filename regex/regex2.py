#演示match对象

import re

regex = re.compile(r'(ab)cd(?P<dog>ef)')

match_obj = regex.search('abcdefghij')

#目标字符串的起始位置
print(match_obj.pos)
print(match_obj.endpos)

# 获取原始的正则表达式对象和目标字符串
print(match_obj.re)
print(match_obj.string)

#获取最后一组的信息
print(match_obj.lastgroup)
print(match_obj.lastindex)
print("==========================")
#获取匹配内容的起止位置
print(match_obj.start())
print(match_obj.end())
print(match_obj.span())

#获取具体匹配内容
print(match_obj.group())
print(match_obj.group(2))

#获取子组内容
print(match_obj.groups())
print(match_obj.groupdict())