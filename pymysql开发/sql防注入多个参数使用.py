import pymysql

if __name__ == '__main__':
    host = 'www.wackyd.top'
    port = 9985
    user = 'test001'
    password = '123456'
    database = 'test002'
    seq1 = '小龙女" or 1 = 1 or "'
    seq2 = '小龙女'
    seq3 = ((10, "二胡班"), (11, "小提琴班"), (20, "小提琴班"))

    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    cursor = conn.cursor()
    # 对数据表完成添加，删除，修改等操作，需要把修改的数据提交到数据库
    sql1 = 'insert IGNORE  into classes values (%s,%s);'
    sql2 = 'update classes set name="少年宫二胡班" where name="二胡班";'
    sql3 = 'delete from classes where name="少年宫二胡班";'
    # 准备sql,使用汉字sql注入的sql语句，%s是sql语句的参数，和字符串格式化里的%s不一样，不要加上引号
    sql4 = 'select * from classes;'

    # print(sql1)

    try:
        result=cursor.executemany(sql1, seq3)
        # 如果没有报错，即执行的sql语句没有问题，接下来就可以提交数据到数据库
        print(result)
        conn.commit()
        cursor.execute(sql4)
        result = cursor.fetchall()
        print(result)

    except Exception as e:
        # 发生错误，需要对刚才执行的sql语句进行撤销，表示数据的回滚（回到没有修改数据之前的状态）
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()
