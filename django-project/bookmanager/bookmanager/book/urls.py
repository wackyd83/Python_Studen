from django.urls import re_path
from book.views import index

urlpatterns=[
    # name就是给url起一个别名
    # 我们可以通过name找到这个路由，name定义视图名称
    re_path(r'.*?',index,name='index'),
    # '''
    # path函数：精准匹配到相应子应用
    # re_path函数：通过正则匹配，符合正则规则的名称都引导至相应子应用
    # '''
]