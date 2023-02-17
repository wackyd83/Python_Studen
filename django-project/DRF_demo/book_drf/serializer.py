from rest_framework import serializers


# 自定义序列化器
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
    btitle = serializers.CharField(max_length=20, min_length=5)
    bpub_date = serializers.DateField()  # required=False:把传递的参数设置为可选
    bread = serializers.IntegerField(max_value=100, min_value=5)
    bcomment = serializers.DateField(default=10)

    # # 返回关联的英雄id:PrimaryKeyRelatedField
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    # 返回关联的英雄模型类的str方法值:StringRelatedField
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)

    # 一对多
    # 返回多个字段，需要使用序列化嵌套
    # heroinfo_set=HeroInfoSerializer(many=True)
