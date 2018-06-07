

# # ２、编写一个闹钟程序，启动时设置定时时间，到时候后打印出一句话，然后程序退出
# import time

# clock_hour = int(input("请设置闹钟小时："))
# clock_minute = int(input("请设置闹钟分钟："))
# clock_second = int(input("请设置闹钟秒钟："))
# clock = (clock_hour,clock_minute, clock_second)
# while True:
#     s = time.time() # 返回当前时间utc秒数
#     d = time.localtime(s)   #　将utc秒数转变为当地时间元组

#     # if clock_hour == d[3] and clock_minute == d[4] and clock_second == d[5]:
#     if clock == d[3:6]:
#         print("时间到了")
#         break
import time

def alarm(hour, minute):
    while True:
        cur_time = time.localtime()  # 返回当地时间元组
        tuple_hm = cur_time[3:5]
        print("%2d:%2d:%2d" % cur_time[3:6], end='\r')
        if (hour, minute) == tuple_hm:
            break

def main():
    hour = int(input("请输入闹钟小时："))
    minute = int(input("请输入闹钟分钟："))
    alarm(hour, minute)
    print("时间到了")

main()
