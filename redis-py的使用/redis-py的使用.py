# 1.导入redis
import redis

if __name__ == '__main__':
    # 2.创建redis的连接实例
    # 在连接/获取外界资源时，一定要注意使用try
    try:
        rs = redis.Redis(host='www.wackyd.top', port=1222, db=0, password='Aa19831220',encoding='utf-8')
        # rs = redis.Redis(host='service.wackyd.top', port=6379, db=0, password='Aa19831220',encoding='utf-8')

    except Exception as e:
        print('报错信息：' + e)

    # 3.操作string
    # 添加set key value
    result = rs.keys('*')
    # resslt=rs.set('b',2)
    # print(resslt)

    for i in result:
        key_type = rs.type(i)
        if key_type=='string'.encode():
            j=rs.get(i)
            i=i.decode('utf-8')
            print(i+'的值是：'+j.decode())
        elif key_type=='hash'.encode():
            j = rs.hkeys(i)
            i = i.decode('utf-8')
            print(i + '的值是：' + str(j))
