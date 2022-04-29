import pymysql
import time


def excute_str():
    star = time.time()

    s = ''
    for i in range(times):
        s += f"('tester{str(i)}'),"

    s = "insert into mytest values" + s
    s = s[0:-1] + ';'

    try:
        cursor.execute(s)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    end = time.time()

    spend = end - star
    print(f'本次SQL操作耗时(excute str拼接10000次后commit)：{spend}秒')


def excutemany_():
    star = time.time()
    s = [f"tester{str(i)}" for i in range(times)]

    try:
        cursor.executemany("insert into mytest values(%s)", s)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    end = time.time()

    spend = end - star
    print(f'本次SQL操作耗时(excutemany 1000次后commit)：{spend}秒')


def excute_for():
    star = time.time()

    try:
        for i in range(times):
            cursor.execute(f"insert into mytest values('tester{i}');")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    end = time.time()

    spend = end - star
    print(f'本次SQL操作耗时(excute for循环1000次后commit)：{spend}秒')


if __name__ == '__main__':
    times = 100000

    conn = pymysql.connect(host='www.wackyd.top', port=9985, user='test001', password='123456', charset='utf8',
                           database='test002')

    cursor = conn.cursor()

    excute_str()
    cursor.execute("select count(*) from mytest;")
    result=cursor.fetchall()
    print(result)
    cursor.execute("truncate table mytest;")
    cursor.execute("select count(*) from mytest;")
    result=cursor.fetchall()
    print(result)

    excutemany_()
    cursor.execute("select count(*) from mytest;")
    result = cursor.fetchall()
    print(result)
    cursor.execute("truncate table mytest;")
    cursor.execute("select count(*) from mytest;")
    result = cursor.fetchall()
    print(result)

    excute_for()
    cursor.execute("select count(*) from mytest;")
    result = cursor.fetchall()
    print(result)
    cursor.execute("truncate table mytest;")
    cursor.execute("select count(*) from mytest;")
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conn.close()
