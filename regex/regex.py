import re 

pattern = r'(ab)cd(ef)'

#　使用re调用findall

# l = re.findall(pattern,'abcdef==abcdef')
# print(l)

#使用正则对象调用findall
regex = re.compile(pattern)
l = regex.findall('abcdef==abcdef',0,6)
print(l)

#通过匹配到的内容分割字符串
l = re.split(r'\s+','hello world\nnihao  china')
print(l)

#替换目标字符串
s = re.sub\
(r'\s+','##','hello world nihao')
print(s)

#比sub多返回一个替换了几处
s = re.subn\
(r'\s+','##','hello world nihao')
print(s)
