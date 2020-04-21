# 验证码随机生成

s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
code = ''
import random
for i in range(4):
	# if i == 3:
		# code += ' '
		# continue
	code += s[random.randint(0,len(s)-1)]

print('你的验证码是：'+code)

user_input = input('请输入你的验证码：')

if user_input.lower() == code.lower():
	print('验证通过！！')
else:
	print('验证码错误！！！！')

