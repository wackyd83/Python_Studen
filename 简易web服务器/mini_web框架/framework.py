# web框架，专门负责处理动态资源请求
import time


# 获取首页数据
def index():
    #  状态信息
    status = '200 OK'
    #  响应头信息
    response_headers = [
        'Server','PWS/1.1'
    ]
    # 1.打开指定的模板文件，读取模板文件中的数据
    with open('template/index.html','r',encoding='utf-8') as f:
        file_data=f.read()
    # 2.查询数据库，把模板里的模板变量({%content%})替换成以后从数据库里面查询的数据
    #  web框架处理后的数据
    data='**************'+time.ctime()+'**************'

    response_body=file_data.replace('{%content%}',data)

    # 返回元组
    return status,response_headers,response_body

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
    if request_path == '/index.html':
        # 获取首页数据

        result=index()
        # 把处理后的结果返回web服务器使用，让web服务器拼接响应报文时使用
        return result
    else:
#         没有动态资源数据，返回404状态信息
        result=not_found()
        return result