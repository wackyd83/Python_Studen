print('\n')
print('*'*50)
print('\t\t用户账号密码登录小练习')
print('*'*50)
print('\n')

email = 'wackyd@163.com'
phone_num = '13828402319'
user_name = 'wackyd'
password = '123456'
input_uname = ''
input_password = ''


def pws_check(input_uname,input_password):
	input_uname = input('请输入你的账号/邮箱/手机号码：')
	input_password = input('请输入你的登录密码：')
	if (input_uname == email or input_uname == phone_num or input_uname == user_name) and input_password == password :
		print('登录成功！')
		return 'secuss'
	else:
			print('\n你输入的账号/密码有误，请重新输入\n')
	
for i in range(3):
	if pws_check(input_uname,input_password)== 'secuss':
		print('正在跳转页面！！')
		break
else:
	print('你输错次数超过{}次，请10分钟后再试'.format(i+1))

