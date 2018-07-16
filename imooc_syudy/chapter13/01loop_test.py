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


# async def get_html(url):
#     print('start get url')
#     await  asyncio.sleep(2)
#     # time.sleep(2)
#     print('end get url')
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html('http://cs.zbj.com') for i in range(10)]
#
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.run_until_complete(asyncio.gather(*tasks))
#     print(time.time() - start_time)


# gather和wait的区别
# gather更加high-level
# group1 = [get_html('http://xxx.com') for i in range(2)]
# group2 = [get_html('http://xxx.com') for i in range(3)]
# group1 = asyncio.gather(*group1)
# group2 = asyncio.gather(*group2)
# group2.cancle()
# loop.run_until_complete(asyncio.gather(group1,group2))





# 获取返回值
async def get_html(url):
    print('start get url')
    await  asyncio.sleep(2)
    return 'yang'


def callback(url, future):
    print(url)
    print('send email to yang')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # get_future = asyncio.ensure_future(get_html('http://sss'))
    task = loop.create_task(get_html('http://sss'))

    # 可以在执行完某一个协程之后，可以添加一个callback逻辑
    # 会把future传给callback，因此需要给callback写一个参数future
    # 假如需要给callback传递一个参数，如url，则需要用偏函数
    # task.add_done_callback(callback)
    task.add_done_callback(partial(callback, 'http://sss.com'))

    # loop.run_until_complete(get_future)
    loop.run_until_complete(task)

    # print(get_future.result())
    print(task.result())


# wait和gather