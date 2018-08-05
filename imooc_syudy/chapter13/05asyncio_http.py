# asyncio没有提供http接口
import asyncio
import socket
from urllib.parse import urlparse


async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    # open_connection是一个协程
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")  # 解码
        all_lines.append(data)
    html = "\n".join(all_lines)
    # print(html)
    return html


async def main():
    tasks = []
    for url in range(20):
        url = "https://www.baidu.com"
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

if __name__ == '__main__':
    import time

    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks = []
    # for url in range(20):
    #     url = "http://shop.projectsedu.com/goods/{}".format(url)
    #     tasks.append(asyncio.ensure_future(get_url(url)))
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print(task.result())

    loop.run_until_complete(main())

    print('cost time is {} seconds'.format(time.time() - start_time))
