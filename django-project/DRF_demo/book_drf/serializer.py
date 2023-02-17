from rest_framework import serializers

# 自定义序列化器
class BookSerializer(serializers.Serializer):

    # 序列化返回字段
    # 根据该字段的模型类定义时的数据类型进行定义
    btitle=serializers.CharField()
    bpub_date=serializers.DateField()
    bread=serializers.IntegerField()
    pass