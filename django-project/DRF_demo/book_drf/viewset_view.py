# ViewSet视图集的使用

from rest_framework.viewsets import ViewSet
# GenericAPIView继承自APIView，并且增加了几个特性:分页、过滤排序
from rest_framework.response import Response  # rest_framework框架自带的response类

from book_drf.serializer import BookSerializer
from books.models import BookInfo


# Create your views here.

class Books(ViewSet):
    # 定义视图类时，如果继承自GenericAPIView，request和response就要使用rest_framework的类
    def list(self, request):
        query_params = request.query_params
        # 1.查询所有图书对象
        books = BookInfo.objects.all()

        ser = BookSerializer(books, many=True)  # 序列化多个对象时，需要加参数many=True

        return Response(ser.data)

    def create(self, request):
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

    # 在ListCreateAPIView类中已封装好get和post方法，因此不需要自己写就可以实现对数据批量查询和新增操作


class BookDRFView(ViewSet):

    '''自定义一个方法名称不是list()、retrieve()、create()、update()、destory()时'''
    def lastdata(self,request,pk):
        book=BookInfo.objects.get(id=pk)
        ser=BookSerializer(book)
        return Response(ser.data)

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)

        ser = BookSerializer(book)  # 序列化单个对象时，无需加参数many=True

        return Response(ser.data)

    def update(self, request, pk):
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
