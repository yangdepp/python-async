# create by 'yang' in 2018/7/15 
__author__ = 'yang'

import asyncio


# 可以给asyncio传递进一些函数执行

def callback(sleep_times):
    print('sleep {} success'.format(sleep_times))


# run_forever不会停止，可以在适当的时候调用这个loop.stop,将当前的loop停止掉
def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # call_soon
    # 第一个参数函数名，即刻执行，在队列中等待下一个循环的时候，立即执行
    # loop.call_soon(callback, 2)
    # loop.call_soon(stoploop, loop)
    # loop.run_forever()  # 此时不会停止

    # call_later
    # 将一个callback在指定的时间去运行
    loop.call_later(2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)
    loop.call_soon(callback, 4)
    loop.run_forever()
