import re

# ^：匹配字符串开头
match_obj=re.match('^\d','7abc')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# $：匹配字符串结尾
match_obj=re.match('.*\d$','3')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')


match_obj=re.match('^\d.*\d$','1sdfsdg3')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# [^47]：表示除了4和7，其他字符都匹配
match_obj=re.match('^\d.*[^47]$','2ssdgasgt8a')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')