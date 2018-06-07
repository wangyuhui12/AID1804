

# 此实例示意如何用实例方法(method)来描述Dog类的行为
class Dog(object):

    @property
    def obj(self):
        print('hello')
    # #
    # @obj.setter
    # def obj(self,value):
    #     self._obj = value


    def eat(self, food):
        '''此方法用来描述小狗吃东西的行为'''
        print("小狗正在吃：", food)

    def sleep(self, hour):
        print("小狗睡了", hour, '小时')

    # @property  # 把方法变成属性调用
    def lob(self):
        print("小狗玩",self.obj)



dog1 = Dog()
# dog1.print()
dog1.eat('狗粮')
dog1.sleep(12)
# # dog1.play('球')  # 对象不能调用不存在的方法
# dog1.obj = '球'
# dog1.lob()
# dog1.obj = '睡'
# dog1.lob()
dog1.obj
