

# 练习：
# 模拟斗地主发牌，牌共５４张，
# 黑桃('\u2660')
# 梅花('\u2663')
# 方块('\u2665')
# 黑桃('\u2666')
# 大小王
# A2-10JQK
# 三个人玩，每个人发１７张牌，底牌留三张
# 操作：
#     输入回车：打印第一个人的１７张牌
#     输入回车：打印第二个人的１７张牌
#     输入回车：打印第三个人的１７张牌
#     输入回车：打印三张底牌

import random
import sys

def poker_list():
    L1 = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    L = []
    for i in L1:
        L.append('\u2660'+' '+i)
        L.append('\u2663'+' '+i)
        L.append('\u2665'+' '+i)
        L.append('\u2666'+' '+i)
    L.append(chr(9819)+' ')
    L.append(chr(9820)+' ')
    return set(L)

def main():
    s = poker_list()
    n = 0
    while True:
        n += 1
        button = input("请输入回车发牌：")
        if button:
           print("输入有误！发牌结束！") 
           sys.exit()
        else:
            L1 = random.sample(s, 17)
            print("第",n,"个人的牌为:",L1)
            s = s - set(L1)         
        if n == 3 :
            break
    button_else = input("请输入回车发牌：")
    if not button_else:
        print("底牌为：",list(s))


if __name__ == '__main__':
    main()
