# random模块
import random

# randmon 0~1之间的随机小数
ran = random.random()
print(ran)

# randrange 在范围内产生步长的随机数，不包括end的数值
ran = random.randrange(1, 10)
print(ran)

# randint 在范围内产生步长的随机数，包前后
ran = random.randint(1, 10)
print(ran)

str1 = '12345m'
list1 = ['张三', '李四', '王五', '赵六']

#在可迭代数据中随机1个字符，并返回字符串
ran=random.choice(str1)
print(ran,type(ran))

#在可迭代数据中随机k个字符，并返回列表，每个元素可能重复
ran = random.choices(str1, k=4)
print(ran, type(ran))

#把列表中的元素重新随机排序后返回原列表
random.shuffle(list1)
print(list1)