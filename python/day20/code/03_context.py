

#　此示例示意环境管理器的定义及使用
class A:
    def __enter__(self):
        print("已进入with语句")
        return self  # 返回的对象将由　as 绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("已离开with语句")

# a = A()  #　创建对象
with A() as a:
    print("这是with语句内的一条语句")

# 已进入with语句
# 这是with语句内的一条语句
# 已离开with语句