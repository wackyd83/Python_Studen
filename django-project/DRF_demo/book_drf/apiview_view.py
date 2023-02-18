
from rest_framework.views import APIView
# APIView继承自View，并且增加了几个特性:权限、认证、限流
from rest_framework.request import Request  # rest_framework框架自带的request类
from rest_framework.response import Response  # rest_framework框架自带的response类

from book_drf.serializer import BookSerializer
from books.models import BookInfo


# Create your views here.

class Books(APIView):
    # 定义视图类时，如果继承自APIView，request和response就要使用rest_framework的类

    def get(self, request):
        query_params=request.query_params
        # 1.查询所有图书对象
        books = BookInfo.objects.all()

        ser = BookSerializer(books, many=True)  # 序列化多个对象时，需要加参数many=True

        return Response(ser.data)

    def post(self, request):
        '''保存数据'''
        # 1.获取参数
        # 使用APIView类后，request的方法改为request.data
        data = request.data

        # 2.校验参数
        ser = BookSerializer(data=data)
        # ser.is_valid(raise_exception=True)  # 序列化器的参数验证方法,raise_exception=True:自动抛出异常进行返回
        ser.is_valid()  # 序列化器的参数验证方法,raise_exception=True:自动抛出异常进行返回
        # ser.validated_data:参数验证的字段数据

        # 3.保存数据
        ser.save()

        # 4.返回结果
        return Response(ser.data)


class BookDRFView(APIView):

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)

        ser = BookSerializer(book)  # 序列化单个对象时，无需加参数many=True

        return Response(ser.data)

    def put(self, request, pk):
        '''更新单一数据'''
        # 1.获取前端数据
        data = request.data

        # 2.验证数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)
        ser = BookSerializer(book, data=data)
        ser.is_valid()

        # 3.更新数据
        ser.save()

        # 4.返回结果
        return Response(ser.data)

    def delete(self, request, pk):
        '''删除数据'''

        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)

        book.is_delete = True
        book.save()

        return Response({})
