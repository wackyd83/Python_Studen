'''
todo list
1.接入服务器，game over后把honour上报服务器
2.game over后显示排行榜
3.出售武器价格为原价0.6
4.enemy_atk会随着honour变大而改用更多骰子


'''

import random
print('*'*50)
print('\t\t王者荣耀')
print('*'*50)
print('\n')

print('*****欢迎进入王者荣耀****\n')

role = input('请选择游戏的角色：\n1.鲁班\n2.后羿\n3.李白\n4.孙尚香\n5.貂蝉\n6.诸葛亮\n')
coins = 100		#自己拥有的金币
weapon_list = []  #自己的武器
honour = 0		#连胜次数

print('欢迎{}来到王者荣耀，赠送金币{}个：'.format(role,coins))

while True:
	if coins <= 50 and len(weapon_list) == 0:
		print('**********GAME OVER!!!!!!!***********')
		break
	choice = input('请选择(1~6)：\n1.购买武器\n2.打仗\n3.出售武器\n4.查看武器\n5.查看当前金币\n6.退出游戏\n')
	if choice == '1':
		print('商店中有以下武器：')
		weapons = [['屠龙刀',500,5],['樱花枪',800,8],['98k',1200,12],['手榴弹',1800,18],['碧血剑',2400,24],['鹅毛扇',3000,30]]
		for weapon in weapons:
			print(weapon[0],weapon[1],'ATK:{}'.format(weapon[2]),sep='\t\t')
		weaponname = input('请选择你需要购买的武器名称：') 
		# 1.原来有没有买过这个武器
		# 2.输入的武器名称是否在武器库
		# 3.钱够不够买武器
		if weaponname not in weapon_list:		#判断是否已经购买过这件武器
			for weapon in weapons:
				if weaponname == weapon[0]:		#判断输入的武器名称是否在商店内
					if coins >= weapon[1]:		#判断钱够不够买武器						
						coins -= weapon[1]
						weapon_list.append(weapon[0])
						print('{}购买{}成功！！'.format(role,weapon[0]))
						break
					else:
						print('金币不足！')
						break

			else:
				print('输入错误，没有{}这件武器'.format(weaponname))
		else:
			print('你已购买了这件武器！')



	if choice == '2':
		print('进入战场......')
		#战斗方式
		#1.选择1件武器
		#2.比大小
		#3.判定胜负
		#4.获得奖励

		
		while True:
			if coins < 50:
				print('金币不足50，{}自动退出战场！'.format{role})
				break
			else:
				print('{}有金币{}，拥有的武器有：'.format(role,coins),weapon_list)
				atk = 0
				enemy_atk = random.randint(1,20)		#默认战斗为每次投掷1个20面骰子
				#选择武器
				fight_weaponname = input('请选择你要使用的武器，如不使用武器请直接回车,退出战斗请输入“exit”：')
				if fight_weaponname in weapon_list:
					coins -= 50
					print('{}进入战斗，扣除50金币'.format(role))
					for i in weapons:
						if fight_weaponname in i:
							atk = i[2] + random.randint(1,20)		#如有武器，则加上武器的加成
							if atk > enemy_atk:
								coins += enemy_atk*10
								honour += 1
								print('战斗胜利！！\n{}获得{}金币奖励\n-----------战绩为：{}场战斗胜利-------------'.format(role,enemy_atk*10,honour))
								# break
							else:
								print('战斗失败！！')
							
				elif fight_weaponname == '':
					coins -= 50
					print('{}进入战斗，扣除50金币'.format(role))
					atk = random.randint(1,20)
					if atk > enemy_atk:
						coins += enemy_atk*10
						honour += 1
						print('战斗胜利！！\n{}获得{}金币奖励\n-----------战绩为：{}场战斗胜利-------------'.format(role,enemy_atk*10,honour))
						# break
					else:
						print('战斗失败！！')


				elif fight_weaponname == 'exit':
					print('{}退出了战斗！！'.format(role))
					break				
				else:
					print('输入错误，你没有{}这件武器！\n'.format(fight_weaponname))




	if choice == '3':
		while True:
			print('{}现在拥有的武器有：'.format(role),weapon_list)
			sale_weapon = input('请输入你要出售的武器的名称，返回请输入“back”：\n')
			if sale_weapon in weapon_list:		#判断你是否拥有要出售的武器
				for i in weapons:				#取出这个武器的价格
					if sale_weapon in i:
						weapon_list.remove(sale_weapon)
						coins += i[1]
						print('出售{}成功！你的金币增加{}'.format(sale_weapon,i[1])) 					
						break
			elif sale_weapon == 'back':
				break

			else:
				print('输入错误，你没有{}这件武器！\n'.format(sale_weapon))


	if choice == '4':
		print('你现在拥有的武器有：',weapon_list)
	if choice == '6':
		if input('请问是否退出游戏（yes/no）：') == 'yes':
			print('退出游戏！！')
			break
	if choice == '5':
		print('你当前金币是：',coins)
else:
	print('输入错误，请重新输入！\n')

