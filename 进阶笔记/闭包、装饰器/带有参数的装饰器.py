
def return_decorator(flag):

    def decorator(func):
        def inner(a,b):
            if flag == '+':
                print('正在努力执行加法计算')
            elif flag == '-':
                print('正在努力执行减法计算')
            func(a,b)
        return inner
    return decorator


@return_decorator('+')
def add_num(a,b):
    result=a+b
    print('加法结果是：',result)

@return_decorator('-')
def sub_num(a,b):
    result=a-b
    print('减法结果是：',result)

add_num(2,4)
sub_num(1,4)