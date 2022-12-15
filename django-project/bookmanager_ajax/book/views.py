import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):

        pass

class ReceiveView(View):

    def get(self,request):

        # 1.接收参数
        data=request.GET
        username=data.get('username')
        password=data.get('password')

        return JsonResponse({'info':{'username':username,'password':password}})

    def post(self,request):

        # 1.接收参数
        # post发送的ajax请求，是个json数据，因此不可以通过request.POST获取数据
        # 因此需要通过request.body获取，并进行decode转码，并使用json.loads()函数进行转换成字符串
        data=json.loads(request.body.decode())
        username=data.get('username')
        password=data.get('password')

        return JsonResponse({'info':{'username':username,'password':password}})
