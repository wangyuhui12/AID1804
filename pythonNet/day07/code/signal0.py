
import signal
from time import sleep

signal.alarm(5)

#　使用默认方法处理SIGALRM
# signal.signal(signal.SIGALRM, signal.SIG_DFL)

#　使用忽略的方法处理SIGALRM
signal.signal(signal.SIGALRM, signal.SIG_IGN)



while True:
    sleep(2)
    print("等待时钟")