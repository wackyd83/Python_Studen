from django.contrib import admin
from django.urls import path,re_path
from . import views,apiview_view,genericapiview_view,mixin_view,childmixin_view,viewset_view,genericviewset_view

urlpatterns = [
    # re_path(r'^books_drf/$', views.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', views.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', apiview_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', apiview_view.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', genericapiview_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', genericapiview_view.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', mixin_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', mixin_view.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', childmixin_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', childmixin_view.BookDRFView.as_view()),

    # # ViewSet路由使用
    # # 把请求方法和自定义方法的名称使用字典做对应
    # re_path(r'^books_drf/$', viewset_view.Books.as_view({'get':'list','post':'create'})),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', viewset_view.BookDRFView.as_view({'put':'update',})),
    # # 当使用ViewSet视图集时，自定义方法名称不是list()、retrieve()、create()、update()、destory()这5个时，需要使用以下的路由定义方式：
    # # 在请求地址后添加自定义名称
    # re_path(r'^book_drf/(?P<pk>\d+)/lastdata/$', viewset_view.BookDRFView.as_view({'get':'lastdata',})),

    # GenericViewSet路由使用
    # 把请求方法和自定义方法的名称使用字典做对应
    re_path(r'^books_drf/$', genericviewset_view.Books.as_view({'get':'list','post':'create'})),
    re_path(r'^book_drf/(?P<pk>\d+)/$', genericviewset_view.BookDRFView.as_view({'put':'update',})),
    # 当使用ViewSet视图集时，自定义方法名称不是list()、retrieve()、create()、update()、destory()这5个时，需要使用以下的路由定义方式：
    # 在请求地址后添加自定义名称
    re_path(r'^book_drf/(?P<pk>\d+)/lastdata/$', genericviewset_view.BookDRFView.as_view({'get':'lastdata',})),
]
