import socket
import threading


def send_msg():
    while True:
        send_content = input()  # input()
        # 对字符串进程编码成为二进制数据
        send_data = send_content.encode("gbk")

        # 3. 发送数据到服务端
        # windows里面的网络调试助手使用的gbk编码
        # linux 里面的络调试助手使用的utf-8编码
        tcp_client_socket.send(send_data)
        if send_content=='exit':
            break
    print('send_msg进程关闭')


def recv_msg():
    while True:
        recv_data = tcp_client_socket.recv(1024)
        # 对二进制数据进行解码
        recv_content = recv_data.decode("gbk")
        print("接收服务端的消息为:", recv_content)
        if not recv_data:

            break
    print('服务器关闭连接')
    print('recv-msg进程关闭')


if __name__ == '__main__':
    # 1. 创建tcp客户端套接字
    # AF_INET: ipv4地址类型
    # SOCK_STREAM： tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 提示: 客户端程序不强制要求绑定端口号
    # tcp_client_socket.bind(("", 1220))
    # 2. 和服务端套接字建立连接
    tcp_client_socket.connect(("127.0.0.1", 1220))
    tcp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    t_send_msg = threading.Thread(target=send_msg, daemon=True)
    # t_send_msg.setDaemon(True)
    print(t_send_msg.daemon)
    t_send_msg.start()

    t_recv_msg = threading.Thread(target=recv_msg,  )
    t_recv_msg.start()
    t_recv_msg.join()

    print('系统关闭')
