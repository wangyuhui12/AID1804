# 02_birthday.py

# 练习：
# 写一个程序，输入你的出生日期
# 　１）算出你已出生了多少天？
# 　２）算出你出生那天是星期几？

import time 

year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))

# 得到出生的UTC秒数
birthday_second = time.mktime((year,
                              month,
                              day, 
                               0,0,0,0,0,0))

# 得到当前时间的秒数
cur_second  = time.time()

s = cur_second - birthday_second
print("您已出生：", s/60/60//24)

birthday = (year, month, day, 0, 0, 0, 0, 0, 0)
# 转为UTC秒数
s = time.mktime(birthday)
# UTC秒数转回到本地日期元组
t = time.localtime(s)
t1 = time.asctime(t)
print(t1)
print(t)
weekday = {
    0:'星期一',
    1:'星期二',
    2:'星期三',
    3:'星期四',
    4:'星期五',
    5:'星期六',
    6:'星期日'
}
print("您出生的那天是：",weekday[t[6]])
