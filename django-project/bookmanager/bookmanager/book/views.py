import json
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from book.models import BookInfo

# Create your views here.
from django.urls import reverse

'''
视图：
1.就是python函数
2.函数的第一个参数就是请求和请求相关的，它是HttpRequest的实例对象.
3.我们必须要返回一个响应，响应是HttpResponse的实例对象/子类实例对象
'''


def index(request):
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # render说明：
    # 1.参数1：当前的请求
    # 2.参数2：模板文件
    # 3.参数3：context传递参数
    name = 'index的变量'
    context = {
        'name': name,
    }

    # 实现业务逻辑
    # 1.先把所有书籍查询出来
    # select * from BookInfo（以前学的SQL语句）
    # ORM模型：
    books = BookInfo.objects.all()
    # books变量存放的是BookInfo实例对象，数据格式为[BookInfo(),BookInfo()]
    # 2.组织数据
    context['books'] = books
    # 3.将组织好的的数据传递给模板
    return render(request, 'index.html', context)


############################################reverse#############################################################
# '''    reverse就是通过name来动态获取路由（路径）
#     如果没有设置namespace，则可以通过name来获取：reverse(name)
#     如果设置了namespace，则可以通过namespace:name来获取：reverse(namespace:name)
# '''
# reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)，viewname 通过视图名字
# 路由是动态获取的
# 如果我们设置了namespace，这时就需要通过namespace:name来获取路由

# path=reverse('index')  # 没有设置namespace
# path = reverse('book:index')  # 设置namespace后的设置方式

# redirect跳转页面
# 1.登录成功后需要跳转到首页
# return redirect('/index/')  # 没有定义视图名称，只能通过路由进行跳转
# return redirect((path))

# 2.注册成功后需要跳转到首页
# return redirect('/index/')  # 没有定义视图名称，只能通过路由进行跳转
# return redirect((path))


'''
使用类似于ipython的东西
python manage.py shell
'''


def detail(request, category_id, book_id):
    # # 1/100
    # # print(category_id, book_id)
    #
    # #####################################GET 查询字符串#########################################################
    # # '''
    # # https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0x8df7d7fd0009b6ef&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=2&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=545&rsv_sug4=545
    # #
    # # 以?作为分隔
    # # ?前表示路由
    # # ?后表示get方式传递的参数，称之为查询字符串
    # # ?key=value&key=value...
    # #
    # # 我们在登录的时候会输入用户名和密码，通常用户名和密码都应该使用POST方式进行传递
    # # 以下例子用get方式传递用户名和密码只用于教学说明，实际项目上不能如此使用
    # # '''
    # query_params = request.GET
    # print(query_params)
    #
    # # http://127.0.0.1:8000/6/10450/?username=wackyd&password=123456
    # # < QueryDict: {'username': ['wackyd'], 'password': ['123456']} >
    # username=query_params.get('username')
    # password=query_params.get('password')
    # print(username,password)
    # #
    # # QueryDict以普通的字典形式来获取意见多值时，只能获取最后的那个值
    # # 我们要获取一键一值的话，就需要使用QueryDict的get方法
    # # 我们要获取一键多值的话，就需要使用QueryDict的getlist方法
    # users=query_params.getlist('username')
    # print(users)
    #
    # #####################################POST 表单数据#########################################################
    #
    # data = request.POST
    # # 获取表单数据后，获取一键一值和获取一键多值的方式跟request.GET一样。
    # # 我们要获取一键一值的话，就需要使用QueryDict的get方法
    # # 我们要获取一键多值的话，就需要使用QueryDict的getlist方法
    # print(data.get('username'))
    # print(data.get('gui'))
    # print(data.getlist('username'))
    #
    # #####################################POST json数据#########################################################
    # '''
    # json数据：json使用双引号
    # {
    #     "name":"wackyd"
    # }
    # '''
    #
    # # POST的json数据放在body中，需要通过request.body获取
    # body = request.body
    # print('body:',body)
    #
    # # b'{\r\n    "username":"wackyd",\r\n    "password":"123456",\r\n    "parameter":"True"\r\n}'
    # # body中的json数据是字节数据，需要转码成字符串格式才能使用。
    # body_str = body.decode()  # python3.6版本后无需进行decode，可直接使用json.loads把他转成字典。
    # print('body_str:',body_str)
    #
    # # 转码后是json形式的字符串，不能直接当字典使用。
    # """
    # json
    # json.dumps  将字典转换成json形式的字符串
    # json.loads  将json形式的字符串转换成字典
    # """
    # """
    # {
    #     "username":"wackyd",
    #     "password":"123456",
    #     "parameter":"True"
    # }
    # """
    # data = json.loads(body_str)
    # print('转换成json后的data：',data)

    #####################################P请求头#########################################################
    # """
    # 在header里面添加的信息，key会自动添加http_前缀
    # 请求头的信息都包含的request.META内。
    # request.META返回的是一个字典，可以直接通过key获取value。
    # """
    #
    # print(request.META)
    # content_type = request.META['CONTENT_TYPE']
    # print(content_type)
    #
    # """
    # method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
    # user：请求的用户对象。
    # path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
    # encoding：一个字符串，表示提交的数据的编码方式。
    #
    # 如果为None则表示使用浏览器的默认设置，一般为utf-8。
    # 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
    # FILES：一个类似于字典的对象，包含所有的上传文件。
    # """
    # print('request.method:', request.method)
    # print('request.user:', request.user)
    # print('request.path:', request.path)
    # print('request.encoding:', request.encoding)
    # print('request.FILES:', request.FILES)

    #####################################跳转页面#########################################################
    # 需求是跳转到首页

    # 每次修改跳转都根据路径，容易出错
    # return redirect('/index/')

    # 通过reverse名字做跳转比较常用
    path=reverse('book:index')
    return redirect(path)


    #####################################JsonResponse#########################################################
    # from django.http import JsonResponse
    # data={'name':'bracke','gender':'male','pwd':'123456'}
    #
    # return JsonResponse(data)
    #
    #####################################HttpResponse#########################################################
    """
    通过HttpResponse传递的数据最好是字符串，如果传递字典等复杂数据，将会导致数据丢失。

    HttpResponse
    content 传递字符串，不要传递对象、字典等复杂数据
    statue  HTTP status code must be an integer from 100 to 599.只能使用系统规定的响应代码。
    content_type    是一个MIME类型
                    语法形式是：大类/小类
                    text/html、text/css、text/javascript
                    application/json
                    image/png、image/git、image/jpeg
    """

    return HttpResponse('datail',status=400)
