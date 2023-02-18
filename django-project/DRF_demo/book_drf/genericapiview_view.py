from rest_framework.generics import GenericAPIView
# GenericAPIView继承自APIView，并且增加了几个特性:分页、过滤排序
from rest_framework.request import Request  # rest_framework框架自带的request类
from rest_framework.response import Response  # rest_framework框架自带的response类

from book_drf.serializer import BookSerializer
from books.models import BookInfo


# Create your views here.

class Books(GenericAPIView):
    # 定义视图类时，如果继承自GenericAPIView，request和response就要使用rest_framework的类

    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    def get(self, request):
        # 1.查询所有图书对象
        books = self.get_queryset()  # 获取查询集中的所有数据

        ser = self.get_serializer(books, many=True)  # 使用指定序列化器，获取序列化器对象

        return Response(ser.data)

    def post(self, request):
        '''保存数据'''
        # 1.获取参数
        # 使用APIView类后，request的方法改为request.data
        data = request.data

        # 2.校验参数
        ser = self.get_serializer(data=data)  # 使用指定序列化器，获取序列化器对象
        # ser.is_valid(raise_exception=True)  # 序列化器的参数验证方法,raise_exception=True:自动抛出异常进行返回
        ser.is_valid()  # 序列化器的参数验证方法,raise_exception=True:自动抛出异常进行返回
        # ser.validated_data:参数验证的字段数据

        # 3.保存数据
        ser.save()

        # 4.返回结果
        return Response(ser.data)


class BookDRFView(GenericAPIView):

    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    def get(self, request, pk):
        try:
            book = self.get_object()  # 从查询集中获取指定的单一数据对象
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)

        ser = self.get_serializer(book)

        return Response(ser.data)

    def put(self, request, pk):
        '''更新单一数据'''
        # 1.获取前端数据
        data = request.data

        # 2.验证数据
        try:
            book = self.get_object()
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)
        ser = self.get_serializer(book, data=data)
        ser.is_valid()

        # 3.更新数据
        ser.save()

        # 4.返回结果
        return Response(ser.data)

    def delete(self, request, pk):
        '''删除数据'''

        try:
            book = self.get_object()
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'}, status=400)

        book.is_delete = True
        book.save()

        return Response({})
