def func_out():
    num1 = 10

    def func_inner():
        nonlocal num1
        num1 = 20  #本质上是修改外部函数变量，其实是在闭包内定义了一个局部变量
        result = num1 + 10
        print(result)

    print('修改前的外部变量：', num1)
    func_inner()
    print('修改后的外部变量：', num1)

    return func_inner


new_func = func_out()
new_func()
