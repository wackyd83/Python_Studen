import socket
import threading
import sys
import framework
import logging

# 在程序入口模块，设置logging日志的配置信息，只配置一次，整个程序都可以使用，好比单例
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s',
                    filename='logx.txt',
                    filemode='a')

class Http_web_server():
    def __init__(self, port):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    def request_handle(self):
        try:
            recv_data = self.new_sockets.recv(4096)
            recv_content = recv_data.decode(encoding='utf-8')
            request_list = recv_content.split(' ', maxsplit=2)
            request_path = request_list[1]
            # print(recv_data)
        except IndexError:
            return

        if request_path == '/':
            request_path = '/index.html'
        #     判断是否动态资源请求，以后把后缀.html的请求认为是动态资源请求

        if '.html' in request_path:
            logging.info('动态资源请求的地址：'+request_path)
            # 动态资源请求：动态资源请求找web框架进行处理，需要把请求参数给web框架
            # 准备给web框架参数信息，都要放到字典里
            env = {
                'request_path': request_path,
                #     传入请求头信息，额外参数可以在字典里面进行添加
            }
            # 使用框架处理动态资源请求：
            # 1.web框架需要把处理结果返回给web服务器
            # 2.web服务器负责把返回结果封装成相应报文发给浏览器
            status,headers,response_body=framework.handle_request(env)
            # print(status,headers,response_body)
            # 响应行
            response_line=f'HTTP/1.1 {status}\r\n'
            # 响应头
            response_header=''
            for header in headers:
                response_header+=f'{header[0]}: {header[1]}\r\n'
            response_data=(response_line+response_header+'\r\n'+response_body).encode('utf-8')
            # 发送响应报文数据给浏览器
            self.new_sockets.send(response_data)
            # 报文发送后关闭sockets连接
            self.new_sockets.close()

        else:
                #     静态资源请求
            logging.info('静态态资源请求的地址：'+request_path)

        # print('静态态资源请求的地址：'+request_path)
            try:
                with open('static' + request_path, 'rb', ) as f:
                    f_data = f.read()
            except FileNotFoundError:
                with open('static/error.html', 'rb', ) as f:
                    f_data = f.read()
                    response_line = 'HTTP/1.1 404 Not Found\r\n'
            else:
                response_line = 'HTTP/1.1 200 OK\r\n'

            response_body = f_data

            response_header = 'Server:PWS/1.0\r\n'

            response = (response_line + response_header + '\r\n').encode('utf-8') + response_body

            self.new_sockets.send(response)

            self.new_sockets.close()

    def start(self):
        while True:
            new_sockets, ip_port = self.tcp_server_socket.accept()
            self.new_sockets = new_sockets
            self.ip_port = ip_port
            print(self.ip_port)

            t = threading.Thread(target=self.request_handle, daemon=True)
            t.start()
            t.join()


def main():
    params=sys.argv  #  获取cmd模式下命令行带入的参数
    if len(params) !=2:
        print('执行的命令行格式如下：python XXXXX.py 端口号')
        logging.warning('在终端启动程序的参数不等于2')
        return
    elif not params[1].isdigit():
        logging.warning('第二个参数的类型必须为数字')

        print('第二个参数必须为数字')
        return

    elif int(params[1]) !=1220:
        logging.warning('第二个参数必须是1220')

        print('第二个参数必须大于1220')
        return

    else:
        port = int(params[1])
    http_server = Http_web_server(1220)
    http_server.start()


if __name__ == '__main__':
    main()
