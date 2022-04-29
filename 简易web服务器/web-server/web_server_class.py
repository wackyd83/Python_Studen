import socket
import threading


class Http_web_server():
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 1220))
        tcp_server_socket.listen(128)
        self.tcp_server_socket=tcp_server_socket


    def request_handle(self):
        try:
            recv_data = self.new_sockets.recv(4096)
            recv_content = recv_data.decode(encoding='utf-8')
            request_list = recv_content.split(' ', maxsplit=2)
            request_path = request_list[1]
        except IndexError:
            return
        try:
            if request_path == '/':
                request_path = '/index.html'
            with open('staic' + request_path, 'rb', ) as f:
                f_data = f.read()
        except FileNotFoundError:
            with open('staic/error.html', 'rb', ) as f:
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

if __name__ == '__main__':
    http_server=Http_web_server()
    http_server.start()