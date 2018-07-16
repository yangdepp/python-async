# create by 'yang' in 2018/7/12 
__author__ = 'yang'


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


for item in gen_fib(10):
    print(item)
