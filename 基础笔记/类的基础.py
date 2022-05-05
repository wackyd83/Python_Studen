# 猫

class Cat:
    type = '猫'

    def __init__(self, nickname, age, color):

        self.__nickname = nickname

        self.age = age
        self.color = color

    @property
    def nickname(self):
        # if self.__nickname
        print('------------------>私有化装饰器property')
        return self.__nickname
    @nickname.setter
    def nickname(self,name):
        if len(name) >5:
            self.__nickname = name



    def eat(self, food):
        print('{}喜欢吃{}'.format(self.__nickname, food))

    def catch_mouse(self, weight, color):
        print('{}抓了{}斤重的{}老鼠'.format(self.__nickname, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('乖乖！继续睡觉吧')
        else:
            print('赶紧起床出去抓老鼠！！')

    def show(self):
        return self.__nickname, self.age, self.color

    @classmethod
    def test(cls):
        print('----------------》类方法')
        cls.static_test()
        print(cls.type)

    @staticmethod
    def static_test():
        print('------------>静态方法')
        # Cat.test()

    def __call__(self, *args, **kwargs):
        print('--------------------call')

    # def __del__(self):
    #     print('---------------------->del')


cat1 = Cat('老白', 3, '白')

print(cat1.nickname)

cat1.nickname='white cat'

print(cat1.nickname)
