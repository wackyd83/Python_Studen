from django.contrib import admin
from django.urls import path,re_path
from . import views,apiview_view,genericapiview_view,mixin_view,childmixin_view

urlpatterns = [
    # re_path(r'^books_drf/$', views.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', views.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', apiview_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', apiview_view.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', genericapiview_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', genericapiview_view.BookDRFView.as_view()),
    # re_path(r'^books_drf/$', mixin_view.Books.as_view()),
    # re_path(r'^book_drf/(?P<pk>\d+)/$', mixin_view.BookDRFView.as_view()),
    re_path(r'^books_drf/$', childmixin_view.Books.as_view()),
    re_path(r'^book_drf/(?P<pk>\d+)/$', childmixin_view.BookDRFView.as_view()),
]
