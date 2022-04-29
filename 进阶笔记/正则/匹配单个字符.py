import re

# .：匹配任意1个字符（除了\n)
match_obj=re.match('t.o','tno')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# []：匹配中括号中列举的任一字符
match_obj=re.match('葫芦娃[12]','葫芦娃2')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# \d：表示0-9的任一数字。
match_obj=re.match('\d','335544')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# \D：匹配一个非数字字符
match_obj = re.match('\d', '335544')
if match_obj:
    result = match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# \s：匹配一个空白字符，空格或者tab键
match_obj=re.match('葫芦娃\s[12]','葫芦娃 2')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# \S：匹配一个非空白字符
match_obj=re.match('葫芦娃\S','葫芦娃 2')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# 匹配某网站中密码的其中一位，密码是由字母、数字、下划线组成
# \w：匹配一个字母、数字、下划线、汉字
match_obj=re.match('\w','_')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')

# \W：匹配一个非字母、非数字、非下划线、非汉字的字符
match_obj=re.match('\W','%')
if match_obj:
    result=match_obj.group()
    print(result)
else:
    # 匹配失败，match_obj是None。
    print('匹配失败')