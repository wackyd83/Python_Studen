# 生成器：根据程序员制订的算法规则循环生成数据，当条件不成立时生成数据就结束。
# 提示：不是把所有数据一次性生成，而是每试用一次生成一次，这样可以节省大量的内存空间。

# 生成器的创建有2种方式：
# 1.生成器推导式：把列表推导式中的中括号改成小括号即可
my_generator1 = (value * 2 for value in range(3))
print(my_generator1, id(my_generator1))

# 2.yield关键字：只要在函数里面看到有yield，那么这个函数可以认为是一个生成器
def my_generator2():
    for i in range(3):
        yield i

result = my_generator2()
print(result, id(result))

# 生成器取值使用next函数获取生成器中的下一个值。
value = next(my_generator1)
print(value)
value = next(my_generator1)
print(value)
value = next(my_generator1)
print(value)
# 当生成器已经没有值时，会跑出StopIteration，表示生成器生成数据完毕
value = next(my_generator1)
print(value)

while True:
    try:
        value = next(my_generator1)
        print(value)
    except StopIteration as e:
        print(e)
        break

# for循环内部循环调用next函数获取生成器中的下一个值，当出现异常，for循环内部自动进行了异常捕获。
for value in my_generator1:
    print(value)