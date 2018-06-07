


# 练习：
# 　１、一个球１００米高空落下，每次落下后反弹高度是原高度的一半，再落下，
# 写程序算出皮球
# １）在第１０次落地后反弹高度是多少，
# ２）、打印出球共经过了多少米的路程

def ball_high(n):
    if n == 0:
        return 100
    else:
        return ball_high(n-1) / 2

def ball_distance(n):
    s = 0
    for i in range(1,n+1):
        s += ball_high(i-1) + ball_high(i)
    return s

print("在第10次落地后的反弹高度为：",ball_high(10))
print("球共经过了路程：",ball_distance(10))