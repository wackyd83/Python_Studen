# 通用的装饰器：可以装饰任意类型的函数

# --------------带有参数的函数-----------------
# def decorator(func):
#     # 使用装饰器装饰已有函数时，内部函数的类型和要装饰的已有函数的类型保持一致
#     def inner(arg1,arg2):
#         print('正在努力执行加法运算')
#         func(arg1,arg2)
#     return inner
#
# @decorator
# def add_num(num1,num2):
#     result=num1+num2
#     print('结果为：',result)
#
# add_num(2,5)


# --------------带有参数和返回至的函数-----------------
# def decorator(func):
#     # 使用装饰器装饰已有函数时，内部函数的类型和要装饰的已有函数的类型保持一致
#     def inner(arg1,arg2):
#         print('正在努力执行加法运算')
#         num=func(arg1,arg2)
#         return num
#     return inner
#
# @decorator
# def add_num(num1,num2):
#     result=num1+num2
#     return  result
#
# result=add_num(2,3)
# print('结果为：',result)


# --------------带有不定长参数和返回至的函数-----------------
# 该装饰器还可以称为通用的装饰器
def decorator(func):
    # 使用装饰器装饰已有函数时，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(*args,**kwargs):
        print('正在努力执行加法运算')
        # *args：把元组里的每一个元素，按照位置参数的方式进行传参
        # **kwargs：把字典里的每一个键值对，按关键字的方式进行传参
        # 这里对元组和字典进行拆包，仅限于结合不定长参数的函数使用
        num=func(*args,**kwargs)
        return num
    return inner

# @decorator
# def add_num(*args,**kwargs):
#     result=0
#         #  args：元组类型
#     #  kwargs：字典类型
#
#     for  value in args:
#         result+=value
#     for value in kwargs.values():
#         result+=value
#
#     return  result
#
# result=add_num(5,3,1,2,9)
# print('结果为：',result)
@decorator
def show():
    print('哈哈')

show()

