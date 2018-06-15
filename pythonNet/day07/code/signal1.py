
from signal import *
import time

#　信号处理函数
def handler(sig, frame):
    if sig == SIGALRM:
        print("接受到时钟信号")
    elif sig == SIGINT:
        print("就不结束")


# 当接受到SIGALRM信号时　用handler函数处理
signal(SIGALRM, handler)
signal(SIGINT, handler)
pause()

# while True:
#     print("waiting fro a signal")
#     time.sleep(2)

