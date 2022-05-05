# time模块
# 时间戳
import time

# 获取时间戳
t = time.time()
print(t, type(t))

# time.sleep(1 )


# 将时间戳转时间
t3 = time.ctime(t)
print(t3)

# 将时间戳转元组

t1 = time.localtime(t)
print(t1)
print(t1.tm_year, t1.tm_mon, t1.tm_mday)
print('---------------------->\n', time.localtime().tm_hour, time.localtime().tm_min)

# 元组转时间戳
t2 = time.mktime(t1)
print(t2)

# 元组转字符串格式
str_t = time.strftime('%Y/%m/%d %H:%M:%S', t1)
print(str_t)

# 字符串转元组
print(time.strptime('1983/12/20', '%Y/%m/%d'))

test = time.struct_time((2020, 5, 21, 17, 9, 52, 3, 142, 0))

print(time.strftime('%Y/%m/%d', test))

# datetime模块

import datetime

timedelta = datetime.timedelta(weeks=1)

now = datetime.datetime.now()
print(now)

reslut = now + timedelta

print(reslut)
