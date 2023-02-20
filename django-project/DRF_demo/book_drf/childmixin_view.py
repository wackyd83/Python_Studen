# 拓展类子类视图

from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
# GenericAPIView继承自APIView，并且增加了几个特性:分页、过滤排序
from rest_framework.response import Response  # rest_framework框架自带的response类

from book_drf.serializer import BookSerializer
from books.models import BookInfo


# Create your views here.

class Books(ListCreateAPIView):
    # 定义视图类时，如果继承自GenericAPIView，request和response就要使用rest_framework的类

    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    # 在ListCreateAPIView类中已封装好get和post方法，因此不需要自己写就可以实现对数据批量查询和新增操作


class BookDRFView(RetrieveUpdateDestroyAPIView):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    # 在RetrieveUpdateDestroyAPIView类中已封装好get、put、delete方法，因此不需要自己写就可以实现对单一数据的查、改、删除（逻辑删除）操作
