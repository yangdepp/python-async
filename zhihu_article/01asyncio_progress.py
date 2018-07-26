# create by 'yang' in 2018/7/16 
__author__ = 'yang'


# 本文章相关代码来自知乎的《谈谈Python协程技术的演进》

# python2.5中，yield关键字加入，生成器有了记忆功能，下一次生成器取值可以恢复到生成器上一次yield执行的位置
# python2.5中，还加入了send方法，与yield搭配使用，可以往暂停的位置通过send方法传入一个值改变状态z

# example 1
def jump_range(up_to):
    step = 0
    while step < up_to:
        jump = yield step
        print('jump', jump)
        if jump is None:
            jump = 1
        step += jump
        print('step', step)


if __name__ == '__main__':
    iterator = jump_range(10)
    print(next(iterator))
    print(iterator.send(4))
    print(next(iterator))
    print(iterator.send(-1))

# 执行过程分析
# 1、执行jump_range(10)，初始化
# 2、执行next(iterator)，进入函数，遇到yield step，暂时离开while语句，返回step0给next，并执行print打印0
# 3、执行send将4发送给上次yield语句处，将send的值4赋值给jump，打印jump 4 ,打印step 4
# 4、继续执行while语句，遇到yield step，将step也就是4返回给iterator.send(4)，打印出4
# 5、执行next(iterator),继续执行while语句，没有发送，所以，回到原先的yield语句处，jump是None;打印jump,None
# 6、向下执行，打印step 5,继续执行while语句，遇到yield step返回5，到next(iterator)，打印出5
# 7、继续向下执行，iterator.send(-1)，发送-1赋值给jump，打印jump -1，向下执行，打印step 4,
# 8、继续while循环，遇到yield step，将step的值4返回，打印出4，结束

# ---------------------------------------------------------------------------------------------
print('-' * 50)


# ---------------------------------------------------------------------------------------------

# python3.3中，生成器又引入了yield from关键字，yield from实现了生成器调用另外生成器的功能
# 可以轻易的重构生成器，比如将多个生成器连接在一起执行

def gen_3():
    yield 3


def gen_234():
    yield 2
    yield from gen_3()
    yield 4
    return 4


def main():
    yield 1
    waitting = yield from gen_234()
    print(waitting)
    yield 5


for element in main():
    print(element)

# yield from可以从其他生成器中yield一个值，不同生成器之间可以互相通信
# yield from进入其他的生成器，在其他生成器中遇到yield,就返回yield from中，再进入调用的for循环


print('-' * 50)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1


fib = fib(2)
for i in fib:
    print(i)

print('-' * 50)


def consumer():
    status = True
    while True:
        n = yield status
        print('I get {}'.format(n))
        if n == 3:
            status = False


def producer(consumer):
    n = 5
    while n > 0:
        yield consumer.send(n)
        n -= 1


if __name__ == '__main__':
    c = consumer()
    c.send(None)
    p = producer(c)
    for status in p:
        if status is False:
            print('I only want 3,4,5')
            break

    print('over!')

print('-' * 50)

import asyncio


async def compute(x, y):
    print('Compute %s + %s' % (x, y))
    await asyncio.sleep(1)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print('%s + %s = %s' % (x, y, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(2, 5))
loop.close()
