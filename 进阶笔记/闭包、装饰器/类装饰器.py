# 使用类装饰已有函数

class MyDecorator(object):
    def __init__(self,func):
        self.__func=func
    # 实现__call__方法，让对象变成可调用的对象，可调用的对象能够像函数一样调用
    def __call__(self, *args, **kwargs):
#         对已有函数进行封装
        print('课已经讲完！')
        self.__func()

@MyDecorator
def show():
    print('快要放学啦！！')

# 执行show，执行MyDecorator类创建实例对象->show()
show()
# show.func()
