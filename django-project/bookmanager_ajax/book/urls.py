from django.urls import re_path
from . import views

urlpatterns={
    re_path(r'login/',views.LoginView.as_view()),
    re_path(r'rece/',views.ReceiveView.as_view()),
}