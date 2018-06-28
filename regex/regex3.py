#flags演示

import re 

s = '''hello world
Hello Kitty
Nihao China
'''
# regex = re.compile(r'.+',re.S)
# regex = re.compile(r'hello',re.I)
# regex = re.compile(r'^Hello',re.M)

pattern = '''(?P<dog>ab) #dog
\s+ #空
(def)  #def 
'''
regex = re.compile(pattern,re.X | re.I)

l = regex.findall("ab   def")
print(l)
