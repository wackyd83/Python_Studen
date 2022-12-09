from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.
def index(request):
    booklist=BookInfo
    name='天天向上'
    context={
        'name':name,
        'job':'产品经理',
        'booklist':next(booklist)
    }

    return render(request,'index.html',context)
    return HttpResponse('~~~~~~~~~~~~~~~')