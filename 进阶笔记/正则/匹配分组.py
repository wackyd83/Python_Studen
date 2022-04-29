import re

# |：匹配左右任一个表达式
fruit_list = ['apple', 'banana', 'orange', 'pear', 'peach', 'grape']
for value in fruit_list:
    # 根据每一个字符串，使用正则表达式进行匹配
    match_obj = re.match('banana|pear', value)
    if match_obj:
        # 获取匹配结果
        result = match_obj.group()
        print('我想吃的水果：' + result)
    else:
        # 匹配失败，match_obj是None。
        print('我不想吃的水果：', value)

# 匹配出163、126、qq等邮箱
# \.：表示对正则表达式里的.进行转义，变成一个普通点，只能匹配.字符
# (163|126|qq)表示一个分组，出现一个小括号就表示一个分组，分组是从1开始计算
# 如果出现多个小括号，分组的顺序是从左到右依次排序
match_obj = re.match('[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com', 'hello@163.com')
if match_obj:
    # 获取整个匹配的数据，如果使用分组数的话，默认是0
    result = match_obj.group(0)
    # 获取匹配分组数据
    type = match_obj.group(1)
    print(result, type)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# 'qq：157421148'
match_obj = re.match('(qq：)([1-9]\d{4,11})', 'qq：157421148')
if match_obj:
    result = match_obj.group(2)
    # 获取匹配分组数据
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# '<html>hh</html>'
# \num：应用分组num匹配到的字符串
match_obj = re.match('<([a-zA-Z1-6]+)>.*</\\1>', '<html>hh</html>')
if match_obj:
    result = match_obj.group(0)
    # 获取匹配分组数据
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

'<html><h1>www.itcast.cn</h1></html>'
# (?P<name>)  给分组起别名
# (?P=name)  引用别名为name的分组匹配到的字符串
match_obj = re.match('<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>',
                     '<html><h1>www.itcast.cn</h1></html>')
if match_obj:
    result = match_obj.group(0)
    # 获取匹配分组数据
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')
