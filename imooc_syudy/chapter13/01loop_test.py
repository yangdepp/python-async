# 事件循环+回调（驱动生成器）+epoll（IO多路复用）

# asyncio异步并发编程
# 协程要搭配时间循环，才会有意义
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado、gevent、twisted、（scrapy，django channels用于http2.0开发）
# tornado（协程+事件循环完成了高并发），实现了web服务器
# django/flask是传统的阻塞IO编程模型，是web开发框架，
# 本身是不提供web服务器的，不能完成socket编码，部署的时候要搭配实现socket的框架（uwsgi， gunicorn，nginx）
# 部署tornado可以直接部署（nginx+tornado）

import asyncio
import time
from functools import partial


# 协程的调用
# async def get_html(url):
# #     print('start get url')
# #     await asyncio.sleep(2)
# #     # time.sleep(2)
# #     print('end the url')
# #
# # if __name__ == '__main__':
# #     # 协程搭配事件循环使用，asyncio实现
# #     start_time = time.time()
# #     loop = asyncio.get_event_loop()
# #     tasks = [get_html("http://www.baidu.com") for i in range(100)]
# #     loop.run_until_complete(asyncio.wait(tasks))
# #     print('cost {} seconds'.format(time.time() - start_time))

###########################################################################

# 获取协程的返回值

async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    return 'yang'


# 如果回调函数要接收一个参数，需要把这个参数放在前面
def callback(url, future):
    print(url)
    print('send email to yang')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()

    # future和task是两种方式， task实际上是Future的一个子类
    # get_future = asyncio.ensure_future(get_html('http://www.baidu.com'))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    task = loop.create_task(get_html('http://www.baidu.com'))
    # 运行成功后执行回调， 可以用偏函数包装函数，传递参数进回调函数
    task.add_done_callback(partial(callback, 'http://www.baidu.com'))

    loop.run_until_complete(task)
    print(task.result())
