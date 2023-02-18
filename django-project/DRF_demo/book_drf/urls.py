from django.contrib import admin
from django.urls import path,re_path
from . import views,apiview_view

urlpatterns = [
    re_path(r'^books_drf/$', apiview_view.Books.as_view()),
    re_path(r'^book_drf/(?P<pk>\d+)/$', apiview_view.BookDRFView.as_view()),
]
