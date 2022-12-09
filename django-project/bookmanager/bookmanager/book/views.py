from datetime import datetime
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

"""
面试题：
    你是如何理解cookie的？/你谈一谈cookie。
    1.概念
    2.流程（大体流程，从http角度分析）
    3.在开发过程中哪里使用了
    4.你在开发过程中遇到什么印象深刻的地方

保存在客户端的数据叫cookie
    cookie保存在客户端
    cookie是基于域名/ip的
    
    0.概念
    1.流程
        第一次请求过程
        1.我们的浏览器第一次请求服务器时，不会携带任务cookie信息。
        2.服务器接收到请求后，发现请求中没有任何cookie信息。
        3.服务器设置一个cookie，这个cookie设置在响应中。
        4.我们的浏览器接收到这个响应后，发现响应中有cookie信息，浏览器会将cookie信息保存起来。
        
        第二次及其之后的过程
        5.当我们的浏览器第二次及其之后的请求都会携带cookie信息。
        6.我们的服务器接收到请求后，会发现请求中携带的cookie信息，这样就知道是谁发的请求。
    2.看效果        
    3.从http协议角度深入掌握cookie的流程（原理）
        第一次：
            1.第一次请求服务器，不会携带任务cookie信息，请求头中没有任何cookie信息
            2.服务器会为响应设置cookie信息，响应头中有set_cookie信息
        第二次及其之后：
            3.第二次及其之后的请求都会携带cookie信息，请求头中有cookie信息
            4.（可选）在当前我们的代码中，没有再次在响应头中设置cookie，所以响应头中没有set_cookie信息

    问题1：我换了浏览器，还能获取到session信息吗？答：不可以
    
    问题2：我不换浏览器，但删除sessionid，则获取不到session数据
    
    问题3：再去执行get_session时，会重新生成sessionid

保存在服务器端的数据叫session
    session需要依赖于cookie
    如果浏览器禁用了cookie，则session不能实现
    0.概念
    1.流程
        第一次请求：
            1.第一次请求时，可以携带一些信息（用户名/密码），这是cookie中没有任何信息
            2.当服务器接收到这个请求后，进行用户名和密码的验证，验证没有问题可以设置session信息
            3.在设置session信息的同时（session信息保存在服务器端），服务器会在响应头中设置一个sessionid的cookie信息(由服务器自己设置的，不是我们设置的。）
            4.客户端（浏览器）在接收到响应后，会将cookie信息保存起来（保存sessionid的信息）
        第二次及其之后的请求：
            5.第二次及其之后的请求都会携带session id信息
            6.当服务器接收到这个请求之后，会获取到sessionid信息，然后进行验证，验证成功后，则可以获取session信息（session信息保存在服务器端）。
    2.效果
    3.从原理（http）角度
        第一次请求：
            1.第一次请求是，在请求头中没有携带任何cookie信息
            2.我们在设置session时，session会做2件事：
                #   第一件：将数据保存在数据库中
                #   第二件：设置一个cookie信息，这个cookie信息是以sessionid为key，value为自定义信息
                cookie肯定会以响应的形式在响应头中出现
        第二次及其之后的请求：
            3.都会携带cookie信息，特别是sessionid     
"""

def set_cookie(request):

    # 1.先判断有没有cookie信息
    # 先假设就是没有cookie
    # request.COOKIES 可以判断浏览器是否已有cookie信息

    # 2.获取用户名
    username=request.GET.get('username')

    # 3.因为我们假设没有cookie信息，我们服务器就要设置cookie信息
    response=HttpResponse('set_cookie')

    # set_cookie(self,key,value)：
    # max_age单位为秒，默认为None，设置为None时，关闭浏览器后删除cookie
    # 时间是从服务器接收到这个请求时间+秒数计算之后的时间
    response.set_cookie('username',username,max_age=0)

    # 删除cookie的2种方式
    # response.delete_cookie(key)
    # response.set_cookie(key,value,max_age=0)


    # 4.返回响应
    return response

def get_cookie(request):

    # 1.服务器可以接受（查看）cookie信息
    cookies=request.COOKIES
    # cookies就是一个字典
    username=cookies.get('username')
    print(username)

    # 2.得到用户信息就可以继续其他的业务逻辑了

    return HttpResponse(f'get_cookie______{username}')

def set_session(request):

    # 1.第一次请求时，可以携带一些信息（用户名 / 密码），这是cookie中没有任何信息
    print(request.COOKIES)

    # 2.对用户名和密码进行验证
    # 假设认为用户名和密码正确
    # username=request.GET.get('username')
    # pwd=request.GET.get('pwd')
    user_id=3319

    # 3.设置session信息
    # request.session理解为字典
    # 设置session的时候，其实session做了2件事：
    #   第一件：将数据保存在数据库中
    #   第二件：设置一个cookie信息，这个cookie信息是以sessionid为key
    request.session['user_id']=user_id

    # 4.返回响应
    return HttpResponse(f'set_session________{user_id}')

def get_session(request):

    # 1.请求都会携带sessionid信息
    print(request.COOKIES)

    # 2.会获取到sessionid信息，然后进行验证，
    # 验证成功，可以获取session信息
    # request.session 字典
    user_id=request.session['user_id']
    user_id=request.session.get('user_id')

    # 3.返回响应
    return HttpResponse(f'get_session____________user_id:{user_id}')

"""
登录页面
    GET 请求是获取登录的页面
    POST 请求是验证登录（用户名和密码是否正确）
"""

# GET请求获取登录的页面
def show_login(request):

    return render(request)

# POST 请求是验证登录（用户名和密码是否正确）
def veri_login(request):

    return redirect('index')

# 我想由2个视图变为1个视图
def login(request):

    # 我们需要区分业务逻辑
    if request.method=='GET':
        # GET请求是获取登录的页面
        return render(request)
    else:
        # POST请求是验证登录（用户名和密码是否正确）
        return redirect('index')

"""
面向对象：
    类视图是采用面向对象的思路
    1.定义类视图：
        1.继承自view（from django.views import View）
        2.不同的请求方式有不同的业务逻辑
            类视图的方法：直接采用http的请求名字作为我们的函数名。例如:get、post、put、delete
        3.类视图的方法的第二个参数必须是请求实例对象
            类视图的方法必须有返回值，返回值是HttpResponse及其子类
    2.类视图的url引导
"""
from django.views import View
class BookView(View):

    def get(self,request):
        return HttpResponse('get')

    def post(self,request):
        return HttpResponse('post')

    # def put(self,request):
    #     return HttpResponse('put')

    # 没有定义该实例方式时，请求了该方法，则返回405Method Not Allowed

    # 如果定义了一个非http_method_names规定的请求方法名称，则无论如何也没有办法进行调用，因为不能修改http协议
    def oooo(self,request):
        return HttpResponse('oooo')
"""
class Person(object):
    
    # cls是什么？-->Person类
    @classmethod
    def say(cls):
        pass
        
    # selft是什么？-->实例对象
    def eat(selt):
        pass
        
    @satticmethod
    def run():
        pass
        
Person.say()

p=Person()
p.eat()
"""

"""
个人中心页面  --必须登录才能显示
GET 方式展示个人中心
POST    实现个人中心信息的修改
定义类视图实现
"""

from django.contrib.auth.mixins import LoginRequiredMixin
class CenterView(LoginRequiredMixin,View):

    def get(self,request):
        return HttpResponse('centerview_get')

    def post(self,request):
        return HttpResponse('centerview_post')

##########################################模板#############################################################

class HomeView(View):

    def get(self,request):

        # 1.获取数据
        username=request.GET.get('username')

        # 2.组织数据
        context={
            'username':username,
            'age':10,
            'timenow':datetime.now(),
            'friends':['Tom','Jack','Roser'],
            'money':{
                '2020':16000,
                '2019':17000,
                '2021':25000
            },
            'desc':'<script>alert("hot")</script>'
        }

        return render(request,'index.html',context=context)