# 拓展类视图

from rest_framework.generics import GenericAPIView
# GenericAPIView继承自APIView，并且增加了几个特性:分页、过滤排序
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response  # rest_framework框架自带的response类

from book_drf.serializer import BookSerializer
from books.models import BookInfo


# Create your views here.

class Books(GenericAPIView, CreateModelMixin, ListModelMixin):
    # 定义视图类时，如果继承自GenericAPIView，request和response就要使用rest_framework的类

    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    def get(self, request):
        # 1.查询所有图书对象
        # 无需自己写逻辑，拓展类ListModelMixin已自带查询所有数据的方法
        return self.list(request)

    def post(self, request):
        '''保存数据'''
        return self.create(request)


class BookDRFView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    def get(self, request, pk):
        '''获取单一图书'''
        return self.retrieve(request, pk)

    def put(self, request, pk):
        '''更新单一数据'''
        return self.update(request, pk)

    def delete(self, request, pk):
        '''删除数据'''
        return self.destroy(request, pk)
