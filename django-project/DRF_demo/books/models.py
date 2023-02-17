from django.db import models


# Create your models here.

class BookInfo(models.Model):
    # 属性名=属性类型（选项）
    btitle = models.CharField(max_length=50, unique=True, verbose_name='书籍名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # django自动为我们添加了一个属性，这个属性就可以通过书籍查询人物信息
    # peopleinfo_set

    def __str__(self):
        '''定义每个数据对象的显示信息'''
        return self.btitle

    # 查询数据时，返回相应的字段内容

    class Meta:
        db_table = 'tb_books'  # 定义数据表的名称，不使用自动生成的表名
        verbose_name = '图书'
        verbose_name_plural = verbose_name  # 显示的复数名称


class HeroInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
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

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.hname
