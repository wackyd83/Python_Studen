import socket
import threading

def web_server():
    while True:
        try:
            new_sockets, ip_port = tcp_server_socket.accept()
            print(ip_port)
            recv_data = new_sockets.recv(4096)
            recv_content = recv_data.decode(encoding='utf-8')
            request_list = recv_content.split(' ', maxsplit=2)
            request_path = request_list[1]
        except:
            continue

        # print(recv_content)
        # print(recv_list)
        # print(request_path)
        try:
            if request_path=='/':
                request_path='/index.html'
            with open('staic' + request_path, 'rb', ) as f:
                f_data = f.read()
        except:
            with open('staic/error.html', 'rb', ) as f:
                f_data = f.read()
            response_line = 'HTTP/1.1 404 Not Found\r\n'

        else:

            response_line = 'HTTP/1.1 200 OK\r\n'

        response_body = f_data

        response_header = 'Server:PWS/1.0\r\n'

        response = (response_line + response_header + '\r\n').encode('utf-8') + response_body

        new_sockets.send(response)

        new_sockets.close()


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 1220))
    tcp_server_socket.listen(128)


    for i in range(5):

        t=threading.Thread(target=web_server,)
        t.start()
        t.join()



