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
    btitle = serializers.CharField(max_length=20, min_length=2, write_only=True)
    # read_only=True:表示该字段只参与序列化
    bpub_date = serializers.DateField()  # required=False:把传递的参数设置为可选
    bread = serializers.IntegerField(max_value=100, min_value=0)
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
    def validate(self, atts):  # 方法名必须使用validate命名，参数名通常使用atts
        if atts['bread'] < atts['bcomment']:
            raise serializers.ValidationError('阅读量大于评论量')
        return atts

    def create(self, validated_data):
        # 保存数据
        book = BookInfo.objects.create(**validated_data)  # 对字典进行拆包处理
        return book
