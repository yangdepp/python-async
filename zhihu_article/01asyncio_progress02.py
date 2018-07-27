# create by 'yang' in 2018/7/27 
__author__ = 'yang'
import socket

# 用同步的方式抓取baidu一个网页
# def sync_way():
#     for i in range(100):
#         sock = socket.socket()
#         sock.connect(('www.baidu.com', 80))  # 建立连接
#         print('connected')
#         request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(i))
#         sock.send(request.encode('ascii'))  # 发送请求
#         response = b''
#         chunk = sock.recv(4096)
#         while chunk:
#             response += chunk
#             chunk = sock.recv(4096)  # 一次接收4096个字节的
#         print('done!')
#
#
# from time import time
#
# start = time()
#
# sync_way()
#
# end = time()
# print('Cost {} seconds'.format(end - start))
# Cost 39.3694531917572 seconds


# 同步有以下几个问题
# 1、socket连接的建立需要等待，一旦握手建立的时间漫长，就会影响下面流程的正常运行
# 2、socket接收数据的过程是阻塞式的，等待buffer的过程也需要一定时间
# 3、socket的建立连接-接收过程是一个个来的，在没完成一个连接时不能进行其他连接的处理

# print('——' * 50)

# 1、先解决第一个问题：socket的等待。痛点很明显，我们不能一直等待socket的状态发生改变，
# 而是当socket的状态发生改变时，让它告诉我们。可以利用IO复用。
# IO复用的定义：预先告知内核，使内核一旦发现进程指定的一个或多个IO条件就绪，就通知进程

# 可以对上面的代码这样修改

from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()  # 根据平台选择最佳的IO多路机制，比如linux就会选择 select、poll、epoll

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


# 创建一个Future类，代表了协程中等待的"未来发生的结果"
# 例如：在发起网络请求时，socket会在buffer中返回一些数据，这个获取的动作在异步流程中发生的时间不确定
# Future就是用来封装这个未来结果的类，但当socket在某个时间段监测到可读事件，读取到数据了，那么他就会把数据写入Future，并告知Future要执行某些回调动作。


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for callback in self._callbacks:
            callback(self)


# 有了Future，我们可以包装一个AsyncRequest类，用以发起异步请求的操作


class AsyncRequest:
    def __init__(self, host, url, port, timeout=5):
        self.sock = socket.socket()
        self.sock.settimeout(timeout)
        self.sock.setblocking(False)
        self.host = host
        self.url = url
        self.port = port
        self.method = None

    def get(self):
        self.method = 'GET'
        self.request = '{} {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(self.method, self.url, self.host)
        return self

    def process(self):
        if self.method is None:
            self.get()
        try:
            self.sock.connect((self.host, self.port))
        except BlockingIOError:
            pass
        self.f = Future()
        selector.register(self.sock.fileno(), EVENT_WRITE, self.on_connected)
        yield self.f
        selector.unregister(self.sock.fileno())

        self.sock.send(self.request.encode('ascii'))
        chunk = yield from read_all(self.sock)
        return chunk

    def on_connected(self, key, mask):
        self.f.set_result(None)
