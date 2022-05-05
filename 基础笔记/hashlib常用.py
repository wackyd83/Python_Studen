# hashlib
# 加密算法
import hashlib
import random

msg = '天苍苍，野茫茫，风吹草低见牛羊'
len_salt = random.randint(1, 6)
str1 = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'

salt = random.choices(str1, k=len_salt)
print(salt)
md5 = hashlib.md5((msg + str(salt)).encode('utf-8'))
print(md5.hexdigest())
print(len(md5.hexdigest()))
print('*' * 50)

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())
print(len(sha1.hexdigest()))
print('*' * 50)

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())
print(len(sha256.hexdigest()))
print('*' * 50)

password = '123456'

password = hashlib.sha256(password.encode('utf-8'))
account_list = ['sdf', 'gfdhkjsdklfjg']
account_list.append(password.hexdigest())

print(account_list)

pwd = input("请输入你的密码：")
pwd = hashlib.sha256(pwd.encode('utf-8'))
if pwd.hexdigest() in account_list:
    print('登录成功！！！！！')
else:
    print('密码错误！！！！！！！！')
