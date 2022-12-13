from django.urls import re_path

from book.views import index
from book import views

urlpatterns = [
    re_path(r'.*?', index),
    re_path(r'login/', views.LoginView.as_view()),
]
