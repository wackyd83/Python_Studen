from django.http import HttpResponse
from django.shortcuts import render
# from book.models import BookInfo


# Create your views here.
from django.views import View


# def index(request):
#     booklist=BookInfo
#     name='天天向上'
#     context={
#         'name':name,
#         'job':'产品经理',
#         'booklist':next(booklist)
#     }
#
#     return render(request,'index.html',context)
#     return HttpResponse('~~~~~~~~~~~~~~~')

class LoginView(View):
    def get(self,request):

        return HttpResponse('get')

    def post(self,request):

        return HttpResponse('post')