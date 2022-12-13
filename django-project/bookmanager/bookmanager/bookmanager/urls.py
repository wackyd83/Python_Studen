"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from login import views


'''
1.urlpatterns是固定写法，它的值是列表
2.我们在浏览器中输入的路径和 urlpatterns中的每一项顺序进行匹配
    如果匹配成功，则直接引导到相应的模块，后续的匹配结束
    如果匹配不成功（把urlpatterns中每一项都匹配过了），则直接返回404
3.urlpatterns中的元素是url
    url的第一个参数是：正则
        r 转义
        ^ 严格的开始
        $ 严格的结尾
    url的第二个参数是：视图函数名
4.我们在浏览器中输入的网址中，哪些部分参与正则匹配？
    http://ip:port/path/?key=value
    "http://ip:port/"和get、post参数不参与正则匹配
5.如果和当前的某一项匹配成功，则引导到子应用中继续匹配
    如果匹配成功，则停止匹配并返回相应的视图
    如果匹配不成功，则继续和后边工程中的url的每一项继续匹配，直到匹配完每一项。
6.
'''

urlpatterns = [
    # path('admin/', admin.site.urls),  # 使用jinja2模板，必须注释admin后台相关配置及路由，否则会报错

    # 添加一项
    # 只要不是 admin/肯定会匹配到这里
    # 我们就都引导到book子应用
    # 在include的第二个参数中添加一个namespace
    # 这样，我们的name就变为了namespace:name
    # namespace习惯上使用子应用的名字
    re_path(r'.*?',include(('book.urls','book'),namespace='book')),

    path(r'login/',views.LoginView.as_view()),


]
