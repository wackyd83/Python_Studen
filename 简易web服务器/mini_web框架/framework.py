# web框架，专门负责处理动态资源请求
import logging
import pprint
import time
import pymysql
import json

# 路由列表，列表里面的每一条记录都是一个路由
route_list = {
    # '/index.html':index,
    # '/center.html':center
}


# 定义带有参数的装饰器
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器时，就要把路由添加到路由列表里
        # 当装饰函数时只添加一次路由即可
        route_list[path] = func

        def inner():
            result = func()
            return result

        return inner

    # 返回一个装饰器
    return decorator


@route('/index.html')
# 获取首页数据
def index():
    #  状态信息
    status = '200 OK'
    #  响应头信息
    response_headers = [
        'Server', 'PWS/1.1'
    ]
    # 1.打开指定的模板文件，读取模板文件中的数据
    with open('template/index.html', 'r', encoding='utf-8') as f:
        file_data = f.read()
    # 2.查询数据库，把模板里的模板变量({%content%})替换成以后从数据库里面查询的数据
    #  web框架处理后的数据
    # 创建连接对象
    conn = pymysql.connect(host='www.wackyd.top', port=9985, user='test001', password='123456', database='stock_db',
                           charset='utf8mb4')
    # data = '**************' + time.ctime() + '**************'
    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = 'select * from info;'

    try:
        # 执行sql
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # print(result)
    except Exception as e:
        # 发生错误，需要对刚才执行的sql语句进行撤销，表示数据的回滚（回到没有修改数据之前的状态）
        # conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()
    data = ''
    # 遍历每一条数据，完成数据的tr标签的封装
    for row in result:
        data += '''
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
            </tr>
            ''' % row

    response_body = file_data.replace('{%content%}', data)

    # 返回元组
    return status, response_headers, response_body

@route('/center_data.html')
# 个人中心数据接口
def center_data():
    #     从数据库吧数据查询出来，然后把查询处理的数据转成json数据
    conn = pymysql.connect(host='www.wackyd.top', port=9985, user='test001', password='123456', database='stock_db',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = 'select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info i inner join focus f on i.id=f.info_id;'

    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    # print(result)
    #     把元组转成列表字典
    #     result_json=[{'code':row[0],'short':row[1],'turnover':row[2],'price':row[3],'highs':row[4],'note_info':row[5]} for row in result]
    center_data_list = [
        {
            'code': row[0],
            'short': row[1],
            'chg': row[2],
            'turnover': row[3],
            'price': str(row[4]),
            'highs': str(row[5]),
            'note_info': row[6],
        }
        for row in result
    ]
    # pprint.pprint(center_data_list)
    result_json = json.dumps(center_data_list,ensure_ascii=False)
    # ensure_ascii=False  表示在控制台能够显示中文
    status = '200 OK'
    response_headers = [
        ('Server', 'PWS/1.1'),
        # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
        ('Content-Type', 'text/html;charset=utf-8')

    ]
    return status,response_headers,result_json


@route('/center.html')
def center():
    #  状态信息
    status = '200 OK'
    #  响应头信息
    response_headers = [
        'Server', 'PWS/1.1'
    ]
    # 1.打开指定的模板文件，读取模板文件中的数据
    with open('template/center.html', 'r', encoding='utf-8') as f:
        file_data = f.read()
    # 2.查询数据库，把模板里的模板变量({%content%})替换成以后从数据库里面查询的数据
    #  web框架处理后的数据

    response_body = file_data.replace('{%content%}', 'aaaaaaaaaaaaaaaa')

    # 返回元组
    return status, response_headers, response_body


# 处理没有找到的动态资源
def not_found():
    #  状态信息
    status = '404 Not Found'
    #  响应头信息
    response_headers = [('Server', 'PWS/1.1')]
    #  web框架处理后的数据
    data = 'not found'
    # 返回元组
    return status, response_headers, data


# 处理动态资源请求
def handle_request(env):
    # 活动动态的请求资源路径
    request_path = env['request_path']
    print('动态资源请求的地址：', request_path)
    # 判断请求的动态资源路径，选择指定的函数处理对应的动态资源请求
    if request_path in route_list:
        result = route_list[request_path]()
    else:
        result = not_found()
        logging.error('没有设置相关的路由信息：'+request_path)
    return result


#     if request_path == '/index.html':
#         # 获取首页数据
#
#         result=index()
#         # 把处理后的结果返回web服务器使用，让web服务器拼接响应报文时使用
#         return result
#     else:
# #         没有动态资源数据，返回404状态信息
#         result=not_found()
#         return result

if __name__ == '__main__':
    pprint.pprint(center_data())
