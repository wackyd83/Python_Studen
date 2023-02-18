from rest_framework import serializers

# 自定义序列化器
from books.models import BookInfo


class HeroInfoSerializer(serializers.Serializer):
    '''英雄序列化器'''
    hname = serializers.CharField()
    hcomment = serializers.CharField()

    # 多对一
    # hbook=serializers.PrimaryKeyRelatedField(read_only=True)
    hbook = serializers.StringRelatedField()


class BookSerializer(serializers.Serializer):
    # 序列化返回字段
    # 根据该字段的模型类定义时的数据类型进行定义
    # write_only = True:表示该字段只参与反序列化
    btitle = serializers.CharField(max_length=20, min_length=2)
    # read_only=True:表示该字段只参与序列化
    bpub_date = serializers.DateField()  # required=False:把传递的参数设置为可选
    bread = serializers.IntegerField(max_value=500, min_value=0)
    bcomment = serializers.IntegerField(default=10)

    # # 返回关联的英雄id:PrimaryKeyRelatedField
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    # 返回关联的英雄模型类的str方法值:StringRelatedField
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)

    # 一对多
    # 返回多个字段，需要使用序列化嵌套
    # heroinfo_set=HeroInfoSerializer(many=True)

    '''自定义验证方法：'''

    # 单一字段验证
    def validate_btitle(self, value):  # 方法名必须使用validate_字段名的方式命名，参数名通常使用value
        if value == 'python':
            raise serializers.ValidationError('书名不能是python')
        return value

    # 多个字段验证
    # def validate(self, atts):  # 方法名必须使用validate命名，参数名通常使用atts
    #     if atts['bread'] < atts['bcomment']:
    #         raise serializers.ValidationError('阅读量大于评论量')
    #     return atts

    def create(self, validated_data):
        # 保存数据
        book = BookInfo.objects.create(**validated_data)  # 对字典进行拆包处理
        return book

    def update(self, instance, validated_data):
        # 更新数据
        instance.btitle=validated_data['btitle']
        instance.bread=validated_data['bread']
        instance.save()
        return instance

# 模型类序列化器
# class BookModelSerialzier(serializers.ModelSerializer):
#     # 修改序列化器中的限制
#     # 1.显示指明字段
#     bread=serializers.IntegerField(max_value=100,min_value=20)
#
#     # 新增原来模型类没有的字段
#     # 新增字段与指定模型类中的字段方法一起用时，必须把新增的字段也包含在fields指定的字段内。
#     sms_code=serializers.CharField(max_length=6,min_length=6)
#
#     class Meta:
#         model=BookInfo  # 指定生成字段的模型类
#         # fields=('btitle','bread')  # 指定模型类中的字段
#         fields='__all__'  # 指定模型类中的所有字段
#         # exclude=('btitle')  # 除指定字段外，模型类中的其他字段
#
#         # 2.添加修改字段的限制选项参数
#         extra_kwargs={
#             'bcomment':{
#                 'max_value':100
#             },
#             'btitle':{
#                 'min_length':5
#             }
#         }

        # read_only_fields=('btitle',)