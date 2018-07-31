# 事件循环和协程：从生成器到协程
def child():
    r = '这是子程序'
    yield r
    print('我在yield后面执行')


def main(c):
    while True:
        try:
            c.send(None)
        except StopIteration as e:
            print('子程序运行结束了')
            break


c = child()
main(c)

# 用原生事件驱动

# import socket
# import sys
# from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
#
# sel = DefaultSelector()
# times = 100
#
#
# def fetch():
#     sock = socket.socket()
#     sock.setblocking(False)
#     try:
#         sock.connect(('www.baidu.com', 80))
#     except BlockingIOError as e:
#         pass
#
#     # 将事件注册进selector中，事件名字是EVENT_WRITE，回调函数是write
#     # 当sock连接完毕后，可以进行写操作的时候，就去调用write函数
#     sel.register(sock, EVENT_WRITE, write)
#
#
# def write(conn, mask):
#     req = b'GET / HTTP/1.0\r\n Host:www.baidu.com\r\n\r\n'
#     sel.unregister(conn)
#     conn.send(req)
#     sel.register(conn, EVENT_READ, read)
#
# # 使用循环去驱动它，调用selector.select()函数，就会进行阻塞，
# # 如果有东西返回，那就直接进入到逻辑层
# def loop():
#     while times:
#         events = sel.select()
#         for key, mask in events:
#             callback = key.data
#             callback(key.fileobj, mask)


# 以上逻辑被打乱了，分成了两个部分。
# 第一部分是socket去连接，不知道什么时候完成，完成的时候，就跳到write中

# -----------------------------------------------------------------------
import socket
import sys
import time
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

sel = DefaultSelector()
times = 5


# 先定义一个Future类，用来使得我们的yield恢复运行
class Future():
    def __init__(self):
        self.coro = None

    def add_coro(self, coro):
        self.coro = coro

    # resume使得yield恢复运行
    def resume(self):
        global times
        try:
            self.coro.send(None)
        except StopIteration as e:
            times = times - 1


# 改造fetch函数
def fetch():
    # 1、等socket连接
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('www.baidu.com', 80))
    except BlockingIOError as e:
        pass

    # 2、写socket
    # 创建一个future对象，future对象中保存一个一条协程
    # 这条协程，就是运行这个fetch()函数，
    # 通过事件循环机制，我们在sock可以读，可以写的时候，调用resume来恢复协程的运行
    f = Future()
    sel.register(sock.fileno(), EVENT_WRITE, f.resume)
    yield f
    sel.unregister(sock.fileno())

    req = b'GET / HTTP/1.0\r\n Host:www.baidu.com\r\n\r\n'
    sock.send(req)

    # 3、读socket
    sel.register(sock, EVENT_READ, f.resume)
    yield f
    sel.unregister(sock.fileno())
    data = sock.recv(4096)


# def write(conn, mask):
#     req = b'GET / HTTP/1.0\r\n Host:www.baidu.com\r\n\r\n'
#     sel.unregister(conn)
#     conn.send(req)
#     sel.register(conn, EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(4096)
    if data:
        pass
    else:
        global times
        times -= 1
        sel.unregister(conn)


def Task():
    coro = fetch()
    future = coro.send(None)
    future.add_coro(coro)


def loop():
    while times:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback()
            if times <= 0:
                return


if __name__ == '__main__':
    t1 = time.time()
    for i in range(times):
        Task()
    loop()
    t2 = time.time()
    print('Cost {}'.format(t2 - t1))
