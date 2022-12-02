from django.db import models

# Create your models here.
'''
1.定义模型类
2.模型迁移
    2.1 先生成迁移文件（不会在数据库中生成表，只会创建一个数据表和模型的对应关系）
    2.2 再迁移（会在数据库中生成表）
3.操作数据库

1.ORM
    表-->类
    字段-->属性
2.模型类需要继承自models.Model
3.模型类会自动为我们添加(生成)一个主键
4.属性名=属性类型(选项)
    属性名注意事项:
        ~不用使用python,mysql关键字
        ~不要使用连续下划线(__)
    属性类型:
        ~和mysql类型类似
    选项：
        ~charfiled必须设置max_length
        ~null=True 允许为空
        ~unique=True 唯一
        ~default=0 默认值
        ~verbose_name 主要是admin后台显示的字段名称
    
'''

'''
书籍表：
    id,name,pub_date,readcount,commentcount,is_delete
'''


class BookInfo(models.Model):
    # 属性名=属性类型（选项）
    name = models.CharField(max_length=(50), unique=True, verbose_name='书籍名称')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # 查询数据时，返回相应的字段内容

    class Meta:
        db_table = 'bookinfo'  # 定义数据表的名称，不使用自动生成的表名
        verbose_name = 'wackyd'


class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    # 外键 关联BookInfo表作为外键，外键必须加上on_delete=models.CASCADE参数
    '''
    on_delete参数说明：
        CASCADE：删除作者信息一并删除作者名下的所有书的信息；
        PROTECT：删除作者的信息时，采取保护机制，抛出错误：即不删除Books的内容；
        SET_NULL：只有当null=True才将关联的内容置空；
        SET_DEFAULT：设置为默认值；
        SET( )：括号里可以是函数，设置为自己定义的东西；
        DO_NOTHING：字面的意思，啥也不干，你删除你的干我毛线关系
        '''
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
