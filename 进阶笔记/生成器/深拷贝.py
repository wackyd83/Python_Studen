from copy import *

# 深拷贝：只要发现对象有可变类型，那么就对该对象到最后一个可变类型的每一层对象进行拷贝，
# 拷贝成功后会开辟新的内存空间

# 不可变类型：数字、字符串、元组
num1 = 1
num2=deepcopy(num1)
print(id(num1),id(num2))

tuple1 = (1,2)
tuple2=deepcopy(tuple1)
print(id(tuple1),id(tuple2))

tuple1 = (1,2,[3,4])
tuple2=deepcopy(tuple1)
print(id(tuple1),id(tuple2))
print(id(tuple1[2]),id(tuple2[2]))

tuple2[2].append(5)
print(tuple1,tuple2)

# 如果发现元组里有可变类型，那么，会对元组进行拷贝和资源数列表进行拷贝，
# 拷贝后都会产生一个新的内存空间
# 但是不可变类型不会进行拷贝，因为不可变类型不允许在原有内存空间的基础修改数据

# 可变类型：列表，字典，集合，对于深拷贝来说，也会进行拷贝。如果发现子对象也是可变类型，也会进行拷贝。
# 拷贝后会开辟新的内存空间，存储拷贝后的对象。
list1=[1,[2,3]]
list2=deepcopy(list1)
print(id(list1),id(list2))
print(id(list1[1]),id(list2[1]))

# 无论是浅拷贝还是深拷贝，都是针对可变类型