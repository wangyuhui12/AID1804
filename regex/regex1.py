import re 

#返回匹配结果的迭代对象
it = re.finditer\
(r'[A-Z]\w*','A good boy,Tom')

#调用group()获取匹配内容
for i in it:
    print(i.group())

#类似绝对匹配
obj = re.fullmatch(r'\w*','abcdefg123')
print(obj.group())

#类似在正则前加了^
obj = re.match\
(r'foo','food on the table')
print(obj.group())

#search只能匹配第一处
obj = re.search\
(r'foo','The food on the table,foo')
print(obj.group())