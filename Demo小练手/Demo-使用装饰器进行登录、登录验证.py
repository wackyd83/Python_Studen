# 登录验证

login_status = False

wrong_time = 0


# 检查错误次数是否超过3次
def wrong_time_check(func):
    def inner_func():
        if wrong_time >= 3:
            print('错误次数超过3次，请等待10分钟后再试')
        else:
            func()
    return inner_func


def login():
    global login_status
    global wrong_time
    for i in range(3):
        username = input('请输入你的登录账号：')
        pwd = input('请输入你的登录密码：')
        if username == 'wackyd' and pwd == '123456':
            print('登录成功！！！！')
            login_status = True
            return True
        else:
            wrong_time += 1
            print('账号或密码错误{}次，请重新输入'.format(wrong_time))


# 检查是否已经登录，如未登录则输入账号密码进行登录
def login_check(func):
    def wrapper():
        if login_status:
            func()
        else:
            print('请先登录！！！！！！！')
            if login():
                func()
    return wrapper


@wrong_time_check
@login_check
def bug_ticket():
    print('请选择购票日期：')
    print('请选择购票场次：')


@wrong_time_check
@login_check
def check_movie():
    print('请选择查看的电影：')


check_movie()
bug_ticket()
