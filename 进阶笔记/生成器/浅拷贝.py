from copy import *

# 浅拷贝：只会对可变类型的第一层对象进行拷贝，不会对子对象进行拷贝，
# 拷贝成功后会开辟一个新的内存空间存储拷贝的这个对象

# 不可变类型：数字、字符串、元组

num1 = 1
# copy()表示是一个浅拷贝
num2 = copy(num1)
# 查看后内存地址没有发生变化，说明没有对对象进行拷贝，也就是说没有开辟新的内存空间
print(id(num1), id(num2))
# 对于不可变类型进行浅拷贝，实际上是对应用的一个拷贝，2个变量指向的是一个内存地址

tuple1 = (1, 3)

tuple2 = copy(tuple1)
print(id(tuple1), id(tuple2))
# 得出结论：浅拷贝不会对不可变类型进行拷贝，也就说不会开辟新的内存空间，
# 对于不可变类型的对象进行浅拷贝，实际上是对引用的拷贝，2个变量指向的是同一个内存地址

list1 = [1, 2, 3, [4, 5]]

list2 = copy(list1)
print(id(list1), id(list2))

list1.append(6)
print(list1, list2)

list2[3].append(7)
print(list1, list2)
