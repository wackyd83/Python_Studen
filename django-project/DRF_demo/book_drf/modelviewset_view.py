# ModelViewSet视图集的使用
from rest_framework.decorators import action  # 要自动生成自定义方法的路由，需要使用action装饰器
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    # 自定义方法
    @action(methods=['get'], detail=True)  # methods:指定自定义方法对应的请求方法，detail:路由上如果要带pk参数，则使用detail=True将自动生成带pk参数的路由地址
    def lastdata(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)
        return Response(ser.data)
