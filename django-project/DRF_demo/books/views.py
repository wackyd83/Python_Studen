import json

from django import http
from django.shortcuts import render
from django.views import View
from books.models import BookInfo
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView


# Create your views here.

class BooksView(View):
    '''获取所有和保存'''

    def get(self, request):
        '''获取数据'''
        # 1.查询所有图书对象
        books = BookInfo.objects.all()

        # 2.返回图书数据
        books_list = []
        for book in books:
            books_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
            })

        return http.JsonResponse(books_list,safe=False)

        pass

    def post(self, request):
        '''保存数据'''
        # 1.获取参数
        data=request.body.decode()
        data_dict=json.loads(data)
        btitle=data_dict.get('btitle')
        bpub_date=data_dict.get('bpub_date')
        bcomment=data_dict.get('bcomment')
        bread=data_dict.get('bread')


        # 2.校验参数
        if not all([btitle,bpub_date]):
            return http.JsonResponse({'error':'缺少必填参数'},status=400)


        # 3.保存数据
        book = BookInfo.objects.create(
            btitle=btitle,
            bpub_date=bpub_date,
            bcomment=bcomment,
            bread=bread
        )

        # 4.返回结果
        return http.JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        })


class BookView(View):
    '''获取单一和更新、删除图书'''

    def get(self, request, pk):
        '''获取单一数据'''
        try:
            book=BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return http.JsonResponse({'error':'书籍不存在'},status=400)
        return http.JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        })

    def put(self, request, pk):
        '''更新单一数据'''
        data=request.body.decode()
        data_dict=json.loads(data)
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')
        bcomment = data_dict.get('bcomment')
        bread = data_dict.get('bread')

        if not all([btitle,bpub_date]):
            return http.JsonResponse({'error': '缺少必填参数'}, status=400)

        try:
            book=BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return http.JsonResponse({'error': '书籍不存在'}, status=400)

        book.bread=bread
        book.bpub_date=bpub_date
        book.bcomment=bcomment
        book.btitle=btitle
        book.save()

        return http.JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        })


    def delete(self, request, pk):
        '''删除数据'''

        try:
            book=BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return http.JsonResponse({'error': '书籍不存在'}, status=400)

        book.is_delete = True
        book.save()

        return http.JsonResponse({
        })

