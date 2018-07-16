# create by 'yang' in 2018/7/14 
__author__ = 'yang'

# import asyncio
#
# loop = asyncio.get_event_loop()
# loop.run_forever()  # 不断的循环，不会停止
# loop.run_until_complete()  # 在运行指定的协程后，会停止掉

# 1、loop会被放到future中
# 2、取消future(task)
import asyncio
import time


# async def get_html(sleep_times):
#     print('waiting')
#     await asyncio.sleep(sleep_times)
#     print('done after {}s'.format(sleep_times))
#
#
# if __name__ == '__main__':
#     task1 = get_html(2)
#     task2 = get_html(3)
#     task3 = get_html(3)
#
#     tasks = [task1, task2, task3]
#     loop = asyncio.get_event_loop()
#
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         all_task = asyncio.Task.all_tasks()
#         for task in all_task:
#             print('cancle task')
#             print(task.cancel())
#         loop.stop()
#         loop.run_forever()  # 不加这个会抛异常
#     finally:
#         loop.close()

print('-' * 50)


# 嵌套协程
async def compute(x, y):
    print('Compute %s + %s...' % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print('%s + %s = %s' % (x, y, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(2, 3))
loop.close()
