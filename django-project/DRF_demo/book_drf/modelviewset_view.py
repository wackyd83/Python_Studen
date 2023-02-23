# ModelViewSet视图集的使用
from django.db import DatabaseError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action  # 要自动生成自定义方法的路由，需要使用action装饰器
from rest_framework.pagination import PageNumberPagination  # 原生自带的分页器
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class PageNum(PageNumberPagination):
    '''自定义局部分页器'''

    # 指定控制每页数量的参数
    page_size_query_param = 'page_size'

    # 指定每页最大返回数量
    max_page_size = 3


class Books(ModelViewSet):
    """
    获取所有数据和新增数据

    list:
    返回图书列表数据

    retrieve:
    返回图书详情数据

    latest:
    返回最新的图书数据

    read:
    修改图书的阅读量
    """
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前视图使用的序列化器

    # 局部认证属性，只对该视图类生效
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    # 局部权限属性，只对该视图类生效
    permission_classes = (IsAuthenticated,)

    # 局部用户限流
    throttle_classes = [UserRateThrottle, ]

    # 视图命名
    throttle_scope = 'uploads'

    # 指定过滤字段
    filterset_fields = ('btitle', 'bread')

    # 指定排序方法类
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]

    # 指定排序字段
    ordering_fields = ('id', 'bread')

    # 指定搜索字段
    search_fields = ('btitle', 'bpub_date')

    # 指定使用自定义的分页器
    pagination_class = PageNum

    # 判断请求方法，根据不同的请求方法返回不同的序列化器
    # 这个使用方法较少使用
    def get_serializer_class(self):
        if self.action == 'lastdata':
            return BookSerializer
        else:
            return BookSerializer

    # 自定义方法
    @action(methods=['get'], detail=True)  # methods:指定自定义方法对应的请求方法，detail:路由上如果要带pk参数，则使用detail=True将自动生成带pk参数的路由地址
    def lastdata(self, request, pk):
        raise DatabaseError
        print(self.action)  # self.action:返回自定义请求方法的方法名
        book = BookInfo.objects.get(id=pk)
        ser = self.get_serializer(book)
        return Response(ser.data)
