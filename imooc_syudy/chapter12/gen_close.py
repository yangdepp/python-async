# create by 'yang' in 2018/8/3 
__author__ = 'yang'


def gen_func():
    yield 'http://www.baidu.com'
    yield 2
    yield 3
    return 'yang'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)