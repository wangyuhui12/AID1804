

# 练习：
# 　猜数字游戏：
#     写程序，随机生成一个０～１００之间的数用变量x绑定循环让用户输入一个数y，
#     输出猜数字的结果
#         如果y等于生成的数x，则提示”你猜对了“，打印出猜测的次数并退出
#         如果y小于x则提示”您猜小了
import random

def createNumber():
    x = []
    for i in range(0,101):
        x.append(i)
    return x

def main():
    # x = createNumber() 
    # x = random.choice(x)
    # x = random.randrange(0,101)
    # x = random.choice(list(range(0,101)))

    x = random.randint(1,100)
    n = 0
    while True:
        n += 1
        y = int(input("请输入您猜的数字"))
        if x == y:
            print("恭喜你，中奖了！")
            break
        elif x > y:
            print("您猜小了，请继续！")
        elif x < y:
            print("您猜大了，请继续！")
        if n == 10:
            print("game over")
            break
        
    print(n)


if __name__ == '__main__':
    main()