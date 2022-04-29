import time

# 定义装饰器
def decorator(func):
    def inner():
#         内部函数对已有函数进行装饰
#         获取当前时间
        begin=time.time()
        func()
        end=time.time()
        print(f'函数完成耗时：{end-begin}秒')
    return inner

@decorator
def work(): #  work=decorator(work),work=inner
    for i in range(10000):
        print(i)

work()