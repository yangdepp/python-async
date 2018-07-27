# create by 'yang' in 2018/7/27 
__author__ = 'yang'
import socket


# 用同步的方式抓取baidu一个网页
def sync_way():
    for i in range(100):
        sock = socket.socket()
        sock.connect(('www.baidu.com', 80))  # 建立连接
        print('connected')
        request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(i))
        sock.send(request.encode('ascii'))  # 发送请求
        response = b''
        chunk = sock.recv(4096)
        while chunk:
            response += chunk
            chunk = sock.recv(4096)  # 一次接收4096个字节的
        print('done!')


from time import time

start = time()

sync_way()

end = time()
print('Cost {} seconds'.format(end - start))
# Cost 39.3694531917572 seconds


# 同步有以下几个问题
# 1、socket连接的建立需要等待，一旦握手建立的时间漫长，就会影响下面流程的正常运行
# 2、socket接收数据的过程是阻塞式的，等待buffer的过程也需要一定时间
# 3、socket的建立连接-接收过程是一个个来的，在没完成一个连接时不能进行其他连接的处理

print('——' * 50)

# 1、先解决第一个问题：socket的等待。痛点很明显，我们不能一直等待socket的状态发生改变，
# 而是当socket的状态发生改变时，让它告诉我们。可以利用IO复用。
# IO复用的定义：预先告知内核，使内核一旦发现进程指定的一个或多个IO条件就绪，就通知进程

# 可以对上面的代码这样修改

from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()
sock = socket.socket()
sock.setblocking(False)

try:
    sock.connect(('www.baidu.com', 80))
except BlockingIOError:
    pass


def connected():
    selector.unregister(sock.fileno())
    print('connected')


selector.register(sock.fileno(), EVENT_WRITE, connected)
