import pymysql

if __name__ == '__main__':
    host = 'www.wackyd.top'
    port = 9985
    user = 'test001'
    password = '123456'
    database = 'test002'
    seq1 = '小龙女" or 1 = 1 or "'
    seq2 = '小龙女'

    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    cursor = conn.cursor()
    # 对数据表完成添加，删除，修改等操作，需要把修改的数据提交到数据库
    sql = 'insert into classes(name) values("二胡班");'
    sql = 'update classes set name="少年宫二胡班" where name="二胡班";'
    sql = 'delete from classes where name="少年宫二胡班";'
    # 准备sql,使用汉字sql注入的sql语句，%s是sql语句的参数，和字符串格式化里的%s不一样，不要加上引号
    sql4 = 'select * from students where name=%s; '
    sql4 = 'select * from students; '
    sql4 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = 'students' and table_schema = 'test002';"



    print(sql4)

    try:
        cursor.execute(sql4)
        # 如果没有报错，即执行的sql语句没有问题，接下来就可以提交数据到数据库
        # conn.commit()
        result=cursor.fetchall()
        print(result)
        for value in result:
            for i in value:
                print(i)

    except Exception as e:
        # 发生错误，需要对刚才执行的sql语句进行撤销，表示数据的回滚（回到没有修改数据之前的状态）
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()
