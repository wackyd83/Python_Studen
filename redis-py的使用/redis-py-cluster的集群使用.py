# encodings=utf-8
# ! /usr/bin/python3.8
# 需要在redis服务器redis.conf配置bind的ip地址
# 1.导库
from rediscluster import RedisCluster

if __name__ == '__main__':
    # 2.组织集群的host和端口
    nodes = [{'host': 'service.wackyd.top', 'port': '6379'},
             ]
    try:
        # 3.创建集群实例
        src = RedisCluster(startup_nodes=nodes, decode_responses=True)
        print(src)
    except Exception as e:
        print(e)

    src.set('name', 'son')
