import json

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

    def post(self, request):
        '''保存数据'''
        # 1.获取参数
        data=request.body.decode()
        data_dict=json.loads(data)

        # 2.校验参数
        ser=BookSerializer(data=data_dict)
        ser.is_valid(raise_exception=True)  # 序列化器的参数验证方法,raise_exception=True:自动抛出异常进行返回

        # 3.保存数据
        # book = BookInfo.objects.create(
        #     btitle=btitle,
        #     bpub_date=bpub_date,
        #     bcomment=bcomment,
        #     bread=bread
        # )

        # 4.返回结果
        return http.JsonResponse(ser.errors)

class Book(View):

    def get(self,request,pk):
        try:
            book=BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return http.JsonResponse({'error':'书籍不存在'},status=400)

        ser=BookSerializer(book)  # 序列化单个对象时，无需加参数many=True

        return http.JsonResponse(ser.data, safe=False)

