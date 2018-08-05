# create by 'yang' in 2018/7/15 
__author__ = 'yang'

import asyncio


def callback(sleep_times):
    print('sleep {} success'.format(sleep_times))


def stoploop(loop):
    loop.stop()


# call_later会按照时间延后的先后顺序进行调用
# call_at会在规定的时间之后
if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.call_later(2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)

    # call soon即刻执行，在call_later之前
    loop.call_soon(callback, 2)
    # loop.call_soon(stoploop, loop)  # 停止掉forever
    loop.run_forever()
