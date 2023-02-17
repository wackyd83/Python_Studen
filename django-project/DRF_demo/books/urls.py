from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    re_path(r'^books/$', views.BooksView.as_view()),
]
