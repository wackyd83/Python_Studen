import random

print('*'*50)
print('\t\t掷骰子游戏')
print('*'*50)
print('\n')

print('*****欢迎进入掷骰子游戏****\n')
# name = input('请输入您的用户名：')
coin = 0

print('''
	你的账户余额不足，请充值。

	充值100元可获得30个游戏币，每次充值必须是100的倍数
	''')


# 充值
def recharge():
	while True:
		x = int(input('''
	请输入充值金额:'''))
		if x >=100 and x % 100 == 0:
			print('''
	充值成功！！！''')
			global coin
			coin = coin + int(x * 3 / 100)
			break
		else:
			print('''
	充值失败！

	充值100元可获得30个游戏币，每次充值必须是100的倍数
				''')
			recharge_answer = input('\t请问您是否继续充值？再次充值请输入“y”，退出请输入“n”:')
			if recharge_answer == 'n':
				break

# 掷骰子游戏
def game():
	global coin
	print('*'*50)
	print('\t\t你当前的余额为{}'.format(coin))
	print('\t\t游戏开始')
	print('\t每次游戏扣除2个游戏币')
	print('*'*50)
	print('\n')

	coin -= 2
	bet_guess = input('''
	请输入你下注选项，"大"或者"小"：''')
	t1 = random.randint(1,6)
	t2 = random.randint(1,6)
	result = t1 + t2
	# print(result)  #开奖log
	if (result <= 6 and bet_guess == '小') or (result >6 and bet_guess == '大'):
		print('''
	恭喜中奖！！！
	你获得1个游戏币奖励！！！''')
		coin += 1
	else:
		print('''
	很抱歉，本次你没有中奖
	本次开奖结果为{}
				'''.format(result))


while True:
	recharge()
	if coin <= 0:
		print('\n***************不充值不能玩游戏，请充值！！***************\n')
	else:
		break

while True:
	game()
	if coin < 2:
		print('''
	你的账户余额不足，请问是否充值继续游戏？	''')
		answer = input('''
	继续游戏请输入“y”，退出游戏请输入“n”:''')
		if answer == 'n':
			break
		else:
			recharge()
	elif input('\n是否继续游戏？继续游戏请输入“y”，退出游戏请输入“n”：') == 'n':
		break



