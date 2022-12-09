
"""
中间件的作用：
    每次请求和响应时都会调用

中间件的定义

中间件的使用：我们可以判断每次请求中是否携带了cookie中某些信息

"""
def simple_middleware(get_response):
    # 这里是中间件第一次调用执行的地方
    # print('init1111111111')

    def middleware(request):
        # 这里是请求前
        print('before request')

        response=get_response(request)

        # 这里是 响应后/请求后
        print('after request/response')

        return response

    return middleware