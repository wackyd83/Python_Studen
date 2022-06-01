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

    resslt=rs.set(random.randint(1,1024),data[::(random.randint(1,10))])
    print(resslt)

    #  添加hashkey
    rs.hset('哈希类型数据',data[::(random.randint(1,10))],random.random())

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

        #  删除数据
        rs.delete(key)
