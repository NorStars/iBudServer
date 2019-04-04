# encoding: utf-8
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
import WebsInfo

def handle_sock(sock, address):
    print("连接地址: %s" % str(address))
    msg = '已建立连接！' + "\r\n"
    sock.send(msg.encode('utf-8'))
    while True:
        try:
            data = sock.recv(102400)
            sock.sendall(data)
            s = data
            # s = data.decode('utf-8')
            print(s)
            js = json.loads(s)
            websinfo = WebsInfo.WebsInfo()
            websinfo.__dict__ = js
            print("网页资源为"+websinfo.urlRes+"header为"+websinfo.urlHeader+'类型为'+websinfo.urlType)
            if data == b'exit':
                print("关闭连接-PythonC")
                break
            if data == b'exit\n':
                print("关闭连接-JavaC")
                break
        except ConnectionError as e:
            print("关闭连接-Err")
            break
    sock.close()


if __name__ == '__main__':

    # 创建 socket 对象
    ss = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, 0)

    # 获取本地主机名
    # host = socket.gethostname()
    # host = "172.31.40.71"
    host = "127.0.0.1"

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
