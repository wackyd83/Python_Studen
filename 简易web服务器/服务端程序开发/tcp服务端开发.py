import socket



if __name__ == '__main__':

    # 1. 创建tcp服务端套接字
    # AF_INET: ipv4 , AF_INET6: ipv6
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 2. 绑定端口号
    # 第一个参数表示ip地址，一般不用指定，表示本机的任何一个ip即可
    # 第二个参数表示端口号
    tcp_server_socket.bind(("", 1220))
    # 3. 设置监听
    # 128: 表示最大等待建立连接的个数
    tcp_server_socket.listen(128)
    # 4. 等待接受客户端的连接请求
    # 注意点： 每次当客户端和服务端建立连接成功都会返回一个新的套接字
    # tcp_server_socket只负责等待接收客户端的连接请求，收发消息不使用该套接字
    new_client, ip_port = tcp_server_socket.accept()
    # 代码执行到此，说明客户端和服务端建立连接成功
    # print("客户端的ip和端口号为:", ip_port)
    # 5. 接收客户端的数据
    # 收发消息都使用返回的这个新的套接字
    recv_data = new_client.recv(1024)
    # 对二进制数据进行解码变成字符串
    recv_content = recv_data.decode("utf-8")
    print("接收客户端的数据为:", recv_content)

    send_content = "问题正在处理中..."
    # 对字符串进行编码
    send_data = send_content.encode("utf-8")
    # 6. 发送数据到客户端
    new_client.send(send_data)
    # 关闭服务与客户端套接字，表示和客户端终止通信
    new_client.close()
    # 7. 关闭服务端套接字， 表示服务端以后不再等待接受客户端的连接请求
    tcp_server_socket.close()