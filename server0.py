# encoding: utf-8
#!/usr/bin/python3
'''
@author: Doran
@license: www.ibud.top
@contact: yudongan97@gmail.com
@software: pycharm
@file: server.py
@time: 2019/3/28 9:44
@desc:
'''
import socket
import json
import threading


def handle_sock(sock, address):
    print("连接地址: %s" % str(address))
    msg = '已建立连接！' + "\r\n"
    sock.send(msg.encode('utf-8'))
    while True:
        try:
            data = sock.recv(102400)
            sock.sendall(data)
            print(data)
            if data == b'exit':
                print("关闭连接")
                break
            if data == b'exit\n':
                print("关闭连接")
                break
        except ConnectionError as e:
            print("关闭连接")
            break
    sock.close()


if __name__ == '__main__':

    # 创建 socket 对象
    ss = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, 0)

    # 获取本地主机名
    # host = socket.gethostname()
    host = "47.100.33.134"

    port = 9527

    # 绑定端口号
    ss.bind((host, port))

    # 设置最大连接数，超过后排队
    ss.listen(100)

    while True:
        # 建立客户端连接
        conn, addr = ss.accept()
        client_thread = threading.Thread(target=handle_sock, args=(conn, addr))
        client_thread.start()

