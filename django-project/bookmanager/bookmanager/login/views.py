from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def login(request):
    return HttpResponse('login_index')

from django.views import View


class LoginView(View):

    def get(self, request):

        return render(request,'login.html')
        # return HttpResponse('get_login')

    def post(self,request):

        return HttpResponse('csrf_token 试验post')

class ReceiveView(View):

    def get(self,request):

        pass
