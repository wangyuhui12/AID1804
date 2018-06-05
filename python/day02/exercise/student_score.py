
class Student():

    @property     # 将方法变成属性调用
    def score(self):
        return self._score

    @score.setter 
    # @property本身创建了另一个装饰其@score.setter，负责把一个getter方法变成属性
    def score(self, value):
        if not isinstance(value, int):
            # isinstance 用于判断value是否是整数
            raise ValueError('score must be an integer!')
            # 生成变量错误
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100")
        self._score = value

n = int(input("请输入您的分数："))
s = Student()
s.score = n
# 增加@property，score的调用由s.score变成s.score=n即属性调用
# s.set_score(n)
# print(s.get_score())
print(s.score)