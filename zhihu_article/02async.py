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
import socket
import sys
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

sel = DefaultSelector()
times = 100


def fetch():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('www.baidu.com', 80))
    except BlockingIOError as e:
        pass

    sel.register(sock, EVENT_WRITE, write)


def write(conn, mask):
    req = b'GET / HTTP/1.0\r\n Host:www.baidu.com\r\n\r\n'
    sel.unregister(conn)
    conn.send(req)
    sel.register(conn, EVENT_READ, read)
