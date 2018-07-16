# create by 'yang' in 2018/7/13 
__author__ = 'yang'

from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    'yang1': 'hhhhhh',
    'yang2': 'xxxxxx'
}


# 自己实现一个my_chain
# yield from iterable
def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


for value in chain(my_list, my_dict, range(5, 10)):
    print(value)
print('-' * 50)

for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


# yield form 的定义
def g1(gen):
    yield from gen


def main():
    g = g1()
    g.send(None)

# 1、main是调用方
# 2、g1 是委托生成器
# 3、gen 是子生成器
# yield from 会在调用方与子生成器之间建立一个通道（双向通道）
