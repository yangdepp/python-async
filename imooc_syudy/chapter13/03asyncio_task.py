# 协程的嵌套

import asyncio


async def compute(x, y):
    print('Compute %s + %s...' % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print('%s + %s = %s' % (x, y, result))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(3, 4))
    loop.close()

# ---------------------------------------------------
# 协程中嵌套子协程运行的时序图

# 1、EventLoop会为协程print_sum创建一个Task，由Task驱动协程运行
# 2、执行print_sum会遇到await，执行另一个协程 compute()
# 3、执行compute遇到await，此协程也会进入到一个暂停的状态
# 4、暂停时会直接通知Task，子协程和调用方直接建立一个通道，暂停结束后，由Task唤醒子协程执行下一行代码
# 5、子协程运行完return x + y后会抛一个异常StopIteration,会被print_sum中的await捕捉到，并提取出3+4的值，又一次进入print_sum协程
# 6、print_sum又被激活，执行print，并且抛一个StopIteration，并被Task捕获

