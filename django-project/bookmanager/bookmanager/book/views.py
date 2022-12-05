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

def detail(request,category_id,book_id):

    # 1/100
    print(category_id,book_id)
    return HttpResponse('datail')