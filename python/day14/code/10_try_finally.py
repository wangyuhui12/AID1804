

# 此示例示意try-finally　语句
# 以煎鸡蛋为例
# １、打开天然气
# ２、煎鸡蛋
# ３、关闭天然气

def fry_egg():
    try:
        print("打开天然气")
        count = int(input("请输入鸡蛋个数："))
        print("煎鸡蛋完成，共煎了%d个鸡蛋" % count)
    finally:    
        print("关闭天然气。")

try:
    fry_egg()
except:
    print("程序已转为正常状态。。")
