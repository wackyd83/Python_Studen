# chr  把Unicode码转字符串
chr64 = chr(64)
print(chr64, type(chr64))

# ord 把单个字符转Unicode码(整形）
ord_abc = ord('a')
print(ord_abc, type(ord_abc))

print(ord('天'))
print(ord('地'))

print(bin(112))

print(hex(65535))

print(oct(65535))


class A:
    pass


a = A()
print(isinstance(a, A))

# 标准库常用函数

# print()            打印
# input()            从输入设备输入
# list()             转列表
# str()              转字符串
# set()              转集合
# dict()             转字典
# tuple()            转元组
# int()              转整形
# float()            转浮点
# chr()              把Unicode码转字符串
# ord()              把单个字符转Unicode码(整形）
# bin()              把整形转二进制
# hex()              把整形转十六进制
# oct()              把整形转八进制
# isinstance(a,A)    判断对象a是否属于A类，A类可以是父类
