# 1.导入redis
import random
import string
import redis

if __name__ == '__main__':
    # 2.创建redis的连接实例
    # 在连接/获取外界资源时，一定要注意使用try

    data=string.ascii_letters+string.digits
    try:
        rs = redis.Redis(host='www.wackyd.top', port=1222, db=0, password='Aa19831220.',encoding='utf-8')
        # rs = redis.Redis(host='service.wackyd.top', port=6379, db=0, password='Aa19831220.',encoding='utf-8')

    except Exception as e:
        print('报错信息：' + e)

    # 3.操作string
    # 添加set key value
    resslt=rs.set(''.join(random.choices(data,k=2)),random.randint(1,1024))

    #  操作有返回值，成功返回True，失败返回False
    print(resslt)

    #  添加hashkey
    rs.hset('hash哈希',''.join(random.choices(data,k=6)),random.random())

    #  添加列表类型数据
    rs.lpush('list列表',''.join(random.choices(data,k=4)))

    #  添加无需集合set类型数据
    rs.sadd('set无序集合',random.choice(string.digits))

    #  添加有序集合zset类型数据
    rs.zadd('zset有序集合',{random.choice(string.ascii_letters):random.choice(string.digits)})

    #  查询所有key
    result = rs.keys('*')

    for key in result:
        key_type = rs.type(key)
        if key_type=='string'.encode():
            j=rs.get(key)
            key=key.decode('utf-8')
            print(key+'的值是：'+j.decode())
        elif key_type=='hash'.encode():
            j = rs.hkeys(key)
            key = key.decode('utf-8')
            print(key + '的值是：' + str(j))
        elif key_type=='list'.encode():
            j = rs.lrange(key,0,-1)
            key = key.decode('utf-8')
            print(key + '的值是：' + str(j))
        elif key_type=='set'.encode():
            j = rs.smembers (key)
            key = key.decode('utf-8')
            print(key + '的值是：' + str(j))
        elif key_type=='zset'.encode():
            j = rs.zrange(key,0,-1)
            key = key.decode('utf-8')
            print(key + '的值是：' + str(j))

        #  删除数据
        rs.delete(key)
