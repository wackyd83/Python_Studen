from django import http
from django.shortcuts import render
from django.views import View
# Create your views here.
from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(View):

    def get(self,request):
        # 1.查询所有图书对象
        books = BookInfo.objects.all()

        ser=BookSerializer(books,many=True)  # 序列化多个对象时，需要加参数many=True

        return http.JsonResponse(ser.data,safe=False)

class Book(View):

    def get(self,request,pk):
        try:
            book=BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return http.JsonResponse({'error':'书籍不存在'},status=400)

        ser=BookSerializer(book)  # 序列化单个对象时，无需加参数many=True

        return http.JsonResponse(ser.data, safe=False)


