from django.urls import re_path,path
from book.views import index,detail

urlpatterns=[
    # name就是给url起一个别名
    # 我们可以通过name找到这个路由，name定义视图名称
    re_path(r'index/',index,name='index'),
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

]

