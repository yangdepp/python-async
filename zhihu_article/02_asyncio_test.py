import aiohttp
import asyncio


@asyncio.coroutine
def fetch_page(session, url):
    response = yield from session.get(url)
    if response.status == 200:
        text = yield from response.text()
        print(text)


loop = asyncio.get_event_loop()

session = aiohttp.ClientSession(loop=loop)

tasks = [
    asyncio.ensure_future(
        fetch_page(session, "http://bigsec.com/products/redq/")),
    asyncio.ensure_future(
        fetch_page(session, "http://bigsec.com/products/warden/"))
]

loop.run_until_complete(asyncio.wait(tasks))
session.close()
loop.close()

# 首先实例化一个eventloop，并将其传递给aiohttp.ClientSession使用，session就不用创建自己的
