from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^books_drf/$', views.Books.as_view()),
    re_path(r'^book_drf/(?P<pk>\d+)/$', views.BookDRFView.as_view()),
]
