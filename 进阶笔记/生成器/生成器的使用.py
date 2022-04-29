# arg为斐波那契数列的个数
def fibonacci(arg):
    # 初始化前2个值
    a = 0
    b = 1
    # 记录每次生成个数的索引
    current_index = 0

    # 循环判断条件是否成日
    while current_index < arg:
        result = a
        a, b = b, a + b
        current_index += 1
        yield result

# 创建生成器
f=fibonacci(100)
f_l=[]
for i in range(100):
    f_l.append(next(f))
    print(f_l)


