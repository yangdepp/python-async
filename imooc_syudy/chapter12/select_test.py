# create by 'yang' in 2018/8/2 
__author__ = 'yang'

# 1、epoll并不代表一定比select好
# 2、在并发高的情况下，连接活跃度不是很高，epoll比select好
# 3、 并发性不高，同时连接很活跃，select比epoll好


# 通过非阻塞IO进行http访问
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html

    # 首先解析url
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好，需要while循环不停的去检查状态

    # http协议
    while True:
        try:
            client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
            break
        except OSError as e:
            pass

    # 将所有数据读取完成
    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
