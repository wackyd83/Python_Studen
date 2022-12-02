from django.urls import re_path
from login import views

urlpatterns=[
    re_path(r'^',views.login),
    # '''
    # path函数：精准匹配到相应子应用
    # re_path函数：通过正则匹配，符合正则规则的名称都引导至相应子应用
    # '''
]