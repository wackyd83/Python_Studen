from django.urls import re_path

from book.views import index

urlpatterns = [
    re_path(r'.*?', index)
]
