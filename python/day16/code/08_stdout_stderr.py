
# import sys
#
# sys.stdout.write("hello world\n")
#
# sys.stderr.write("我的出现是个错误！\n")

import time


f = open('info.txt', 'w')
f.write('hello')

time.sleep(15)
print("程序睡醒了，继续执行。")


f.close()