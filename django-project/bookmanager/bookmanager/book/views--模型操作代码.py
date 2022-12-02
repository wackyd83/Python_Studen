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

#################################F对象######################################

# 两个属性怎么比较 F对象
'''
F对象的语法形式
filter(字段名__运算符=F('字段名'))
'''
from django.db.models import F

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 查询阅读量大于等于评论量2倍的图书
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)

#################################Q对象######################################

# 需要查询id大于2，并且阅读量大于20的书籍

# 方式一
# filter().filter()
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)

# 方式二
# filter(条件1,条件2)
BookInfo.objects.filter(id__gt=2,readcount__gt=20)

# 需要查询id大于2，或者阅读量大于20的书籍

from django.db.models import Q

'''
Q(字段名__运算符=值)
或   Q()|Q()
并且  Q()&Q()
not   ~Q()
'''
BookInfo.objects.filter(Q(id__gt=2)|Q(readcount__gt=20))

# 需要查询id不为3
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

#################################聚合函数######################################
'''
Sum,Avg,Max,Min,Count

聚合函数需要使用 aggregate
语法形式是：aggragte(聚合函数('字段'))
'''

# 当前数据的阅读总量
from django.db.models import Sum,Avg,Max,Min,Count
BookInfo.objects.aggregate(Sum('readcount'))

#################################排序######################################
# 默认升序
BookInfo.objects.all().order_by('readcount')
# 降序排序
BookInfo.objects.all().order_by('-readcount')

#################################关联查询######################################
'''
书籍和人物的关系是一对多  1：n
书籍中没有人物关于人物的字段
人物中有关于书籍的字段（book字段）
语法形式:
    1.通过书籍查询人物信息（已知主表数据，关联查询从表数据）
        主表模型.关联模型类名（小写）_set
    2.通过人物查询书籍信息（已知从表数据，关联查询主表数据）
        从表模型（实例对象）.外键
'''
# 查询书籍为1的所有人物信息
# 通过书籍查询人物
# 1.查询书籍
book=BookInfo.objects.get(id=1)
# 2.根据书籍关联人物信息
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
# 根据书籍查询人物
from book.models import PeopleInfo
# 1.查询人物
person=PeopleInfo.objects.get(id=1)
# 2.根据人物关联查询书籍
# person.book是实例对象
person.book
person.book.name

#################################关联查询的筛选######################################
'''
书籍和人物的关系是一对多  1：n
书籍中没有人物关于人物的字段
人物中有关于书籍的字段（book字段）
语法形式:
    1.我们需要的是书籍信息，已知条件是人物信息
    2.我们需要的是主表数据，已知条件是从表信息
        filter(关联模型类名小写__字段__运算符=值)
    3.我们需要的是人物信息，已知条件是书籍信息
    4.我们需要的是从表数据，已知条件是主表信息
        filter(外键__字段__运算符=值)
'''

# 查询图书，要求图书人物为"郭靖"
# 需要的图书，条件是任务
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')  # 简写

# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name__exact='天龙八部')
PeopleInfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)

########################################查询集####################################################

#################################惰性执行######################################
'''
创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用
'''

#################################缓存######################################
'''
缓存：
    内存： 存储容量小，读取速度快，断电即失
    硬盘： 存储容量大，读取速度快，断电保存
    
当前缓存的概念：
    我们把硬盘的数据，暂存在内存中，这样读取速度就很快

'''
[book.id for book in BookInfo.objects.all()]
# 优化一下
books=BookInfo.objects.all()
[book.id for book in books]

#################################限制查询集######################################
# 查看结果集第一、第二项
books = BookInfo.objects.all()[0:2]
books = BookInfo.objects.all()[:2]

#################################分页######################################
from django.core.paginator import Paginator

books=BookInfo.objects.all()

# object_list   结果集/列表
# per_page  每页多少条记录
# object_list,per_page
p=Paginator(books,2)

# 获取第几页的数据
books_page=p.page(1)
# books_page是一个列表，存放该分页的所有数据
books_page[0]


