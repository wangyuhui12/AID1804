
# 练习：
# 　写一个函数　get_score() 来获取学生的成绩(0~100),如果输入出现异常，则此函数返回0，否则返回用户输入的成绩
# def get_score():
#     ...
# score = get_score()
# print("学生的成绩是：", score)

def get_score():
    try:
        score = int(input("请输入学生的成绩:"))
        if score < 0 or score > 100:
            raise ValueError("成绩不合法！")
            return 0
        return score
    except ValueError:
        print("成绩不合法！")
        return 0

    # try:
    #     n = int(input("请输入学生成绩："))
    # except:
    #     return 0

    # try:
    #     if n < 0 or n > 100:
    #         raise ValueError('成绩不合法！')
    # except ValueError as e:
    #     print(e)
    #     return 0
    # return n
    # if 0 <= n <= 100:
    #     return 0
    # return n

score = get_score()
print("学生的成绩是：", score)
