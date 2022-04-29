
# 外部函数接收姓名参数
def config_name(name):
    # 内部函数使用外部函数的参数，并且完成数据显示的拼接
    def func_inner(msg):
        print(name+':'+msg)
    #     外部函数要返回内部函数
    print(id(func_inner))
    return func_inner

# 创建Tom闭包实例（对象）
tom=config_name('Tom')
# 创建Jerry闭包实例
jerry=config_name('Jerry')
# 如果执行Tom闭包，因为已经保存name参数，那么以后再输入的时候都是Tom在说：XXX
tom('你他喵是个球！')
jerry('关你鸟事！！！！')
tom('我是瞄')