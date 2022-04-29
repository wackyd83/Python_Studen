import pymysql

if __name__ == '__main__':
    host = 'www.wackyd.top'
    port = 9985
    user = 'test001'
    password = '123456'
    database = 'test002'
    seq = '小龙女" or 1 = 1 or "'

    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    cursor = conn.cursor()
    # 对数据表完成添加，删除，修改等操作，需要把修改的数据提交到数据库
    sql = 'insert into classes(name) values("二胡班");'
    sql = 'update classes set name="少年宫二胡班" where name="二胡班";'
    sql = 'delete from classes where name="少年宫二胡班";'
    sql4 = f'select * from students where name="{seq}"; '

    print(sql4)

    try:
        cursor.execute(sql4)
        # 如果没有报错，即执行的sql语句没有问题，接下来就可以提交数据到数据库
        # conn.commit()
        result = cursor.fetchall()
        print(result)
    except Exception as e:
        # 发生错误，需要对刚才执行的sql语句进行撤销，表示数据的回滚（回到没有修改数据之前的状态）
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()
