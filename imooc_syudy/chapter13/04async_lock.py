# create by 'yang' in 2018/7/15
import aiohttp as aiohttp

__author__ = 'yang'

import asyncio

# total = 0
#
#
# async def add():
#     global total
#     for i in range(100000):
#         total += 1
#
#
# async def desc():
#     global total
#     for i in range(100000):
#         total -= 1
#
#
# if __name__ == '__main__':
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)

# --------------------------------------------------------------
cache = {}
from asyncio import Lock

lock = Lock()


async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff()


async def use_stuff():
    stuff = await get_stuff()


tasks = [parse_stuff(), use_stuff()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
