from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from book.models import BookInfo

# Create your views here.
'''
视图：
1.就是python函数
2.函数的第一个参数就是请求和请求相关的，它是HttpRequest的实例对象.
3.我们必须要返回一个响应，响应是HttpResponse的实例对象/子类实例对象
'''


def index(request):
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # render说明：
    # 1.参数1：当前的请求
    # 2.参数2：模板文件
    # 3.参数3：context传递参数
    name = 'index的变量'
    context = {
        'name': name,
    }

    # 实现业务逻辑
    # 1.先把所有书籍查询出来
    # select * from BookInfo（以前学的SQL语句）
    # ORM模型：
    books=BookInfo.objects.all()
    # books变量存放的是BookInfo实例对象，数据格式为[BookInfo(),BookInfo()]
    # 2.组织数据
    context['books']=books
    # 3.将组织好的的数据传递给模板
    return render(request, 'index.html', context)

'''
使用类似于ipython的东西
python manage.py shell
'''

########################################新增数据####################################################

from book.models import BookInfo

# 方式一
# 会把新生成的对象返回给我们
book=BookInfo(
    name='python',
    pub_date='2000-01-01'
)
# 需要手动调用save方法
book.save()

# 方式二 直接入库
# objects模型的管理类
# 我们对模型的增删改查都找它
# 把新生成的对象返回给我们
BookInfo.objects.create(
    name='java',
    pub_date='2000-01-01'
)

########################################修改（更新）数据####################################################

from book.models import BookInfo

# 方式一
# 1.先查询数据
# select * from bookinfo where id=1
book=BookInfo.objects.get(id=1)
# 2.直接修改实例的属性
book.readcount=20
# 3.调用save方法
book.save()

# 方式二  直接更新
# filter 过滤
BookInfo.objects.filter(id=1).update(
    readcount=100,
    commentcount=200,
)

########################################删除数据####################################################

# 方式一
# 1.先查询出数据
book=BookInfo.objects.get(id=5)
# 2.调用删除方法
book.delete()

# 方式二
BookInfo.objects.filter(id=6).delete()

########################################查询数据####################################################

#################################基本查询######################################

# get 得到某一个数据
# all 获取所有的数据
# count 获取个数

# 返回一个对象
book=BookInfo.objects.get(id=1)

# 查询id，不存在的数据会抛出异常
book=BookInfo.objects.get(id=100)
'''
BookInfo matching query does not exist.
'''
try:
    book = BookInfo.objects.get(id=2)
# except Exception:
#     pass
except BookInfo.DoesNotExist:
    pass

# 返回所有结果，列表
book=BookInfo.objects.all()

# count
BookInfo.objects.all().count()
BookInfo.objects.count()

#################################filter,get,exclude######################################

'''
# select * from bookinfo where 条件语句
# 相当于where查询
# filter      ：筛选/过滤，返回n个结果（n=0/1/n)
# get         ：返回1个结果
# exclude     ：排除掉符合条件剩下的结果，相当于not
# 语法形式：
#     以filter(字段名__运算符=值)为例
'''

# 查询编号为1的图书
BookInfo.objects.get(id__exact=1)
BookInfo.objects.get(id=1)  # 简化写法

BookInfo.objects.filter(id__exact=1)
book=BookInfo.objects.filter(id=1)  # 简化写法

# 查询书名包含'湖'的图书
# contains 包含
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])

# 查询编号大于3的图书
# gt    大于  great
# gte   大于等于  e equal
# lt    小于  less than
# lte   小于等于
BookInfo.objects.filter(id__gt=3)

# 查询书籍id不为3的图书
BookInfo.objects.exclude(id__exact=3)
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-01-01')
