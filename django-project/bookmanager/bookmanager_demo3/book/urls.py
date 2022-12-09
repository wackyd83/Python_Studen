
from book.views import index
from django.urls import re_path

urlpatterns = [
    re_path('.*?',index),
]