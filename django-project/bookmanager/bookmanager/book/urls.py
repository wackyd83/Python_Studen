from django.urls import re_path,path
from book.views import index,detail,set_cookie,get_cookie,set_session,get_session,BookView,CenterView,HomeView

urlpatterns=[
    # name就是给url起一个别名
    # 我们可以通过name找到这个路由，name定义视图名称
    re_path(r'home/',index,name='index'),
    # '''
    # path函数：精准匹配到相应子应用
    # re_path函数：通过正则匹配，符合正则规则的名称都引导至相应子应用
    # '''

    # 书籍路由:
    # ip:port/category_id/book_id
    # category_id：分类id
    # book_id：书籍id
    # 通过分组获取正则中的数据
    # 1.我们进行正则分组的参数会传递给视图。
    # 2.定义视图的时候需要定义变量来接收参数。

    # 根据位置顺序获取参数
    # re_path(r'(1)/(100)/',detail),
    # re_path(r'(\d+)/(\d+)/',detail),  # 通过正则规定输入的格式来定义路由

    # (?P<name>...)正则中给分组起别名
    # 关键字参数————推荐使用关键字参数
    re_path(r'(?P<category_id>\d+)/(?P<book_id>\d+)/', detail),  # 通过正则规定输入的格式来定义路由

    # cookie的第一次请求
    path('set_cookie/', set_cookie),

    # cookie的第二次及其之后的请求
    path('get_cookie/', get_cookie),

    # session的第一次请求
    path('set_session/', set_session),

    # session的第一次请求
    path('get_session/', get_session),

    # re_path的第一个参数是    正则
    # re_path的第二个参数是    视图函数名
    re_path(r'bookview/',BookView.as_view()),
    re_path(r'centerview/',CenterView.as_view()),
    re_path(r'homeview/',HomeView.as_view()),
]

