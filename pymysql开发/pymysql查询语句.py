# 1.导包
import pymysql

if __name__ == '__main__':
    # 2.创建连接对象
    host = 'www.wackyd.top'
    port = 9985
    user = 'test001'
    password = '123456'
    database = 'jing_dong'

    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset='utf8')

    # 3.获取游标，目的是要执行sql语句
    cursor = conn.cursor()
    sql_select = 'select * from goods'

    # 4.执行sql语句
    cursor.execute(sql_select)

    # 获取查询结果，返回的数据结果是元组
    row = cursor.fetchone()
    print(row)
    # 返回的数据类型是一个元组，其中元组里面的每条数据都是元组
    rows=cursor.fetchall()
    for row in rows:
        print(row)

    # 5.关闭游标
    cursor.close()
    # 6.关闭连接
    conn.close()
