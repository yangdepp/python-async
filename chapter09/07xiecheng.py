# create by 'yang' in 2018/7/14 
__author__ = 'yang'


# python中的yield不但可以返回一个值，它还可以接收调用者发出的参数
# 生产者生产消息后，直接通过yield跳转消费者开始执行，
# 待消费者执行完毕后，切换回生产者继续生产

def MyGenerator():
    value = yield 1
    yield value
    return 'done'


gen = MyGenerator()
print(next(gen))  # 也可以不用next，用send(None)发送一个None
print(gen.send('I am value'))

# 1、首先初始化MyGenerator；
# 2、调用next(gen)，启动生成器，进入MyGenerator，遇到yield 1返回1
# 3、gen.send('I am Value')，则会传入一个字符串，进入上次执行yield的地方，把字符串赋值给value
# 4、再次执行yield value，就返回'I am value'

print('_' * 50)


def consumer():
    r = ''
    while True:

        m = yield r
        if not m:
            return

        print('[CONSUMER] Consuming %s...' % m)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)
    c.close()


c = consumer()
produce(c)
