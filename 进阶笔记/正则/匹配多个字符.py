import re


# *：匹配前一个字符出现0次或多次，即可有可无
match_obj=re.match('t.*o','tsdfsdgwo')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# +：匹配前一个字符至少出现1次
match_obj=re.match('t.+o','tsdfsadfago')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# ?：匹配前一个字符出现0次或者1次
match_obj=re.match('https?','http')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# {m}：匹配前一个字符必须出现m次
match_obj=re.match('ht{2}p?','http')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# {m,n}：匹配前一个字符最少出现m次，最多出现n次
match_obj=re.match('ht{1,6}p','httttp')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# 扩展：{m,}：匹配前一个字符最少出现m次
match_obj=re.match('ht{2,}p','htttttttttp')
if match_obj:
    # 获取匹配结果
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')