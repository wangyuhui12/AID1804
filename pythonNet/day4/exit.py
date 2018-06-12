import os 
import sys 

#进程结束
# os._exit(0)

try:
    sys.exit(1)
except SystemExit as e:
    # e为异常退出状态
    print(e)

print("Process end")