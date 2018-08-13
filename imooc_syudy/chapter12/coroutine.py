# create by 'yang' in 2018/8/3 
__author__ = 'yang'


def gen_func():
    # 可以产出值，可以接收值（调用方传递进来的值）
    html = yield 'http://www.baidu.com'
    print(html)
    yield 2
    yield 3
    return 'yang'

#  1、throw  2、close






# 生成器不只可以产出值，还可以生成值
if __name__ == '__main__':
    gen = gen_func()
    # 启动生成器
    # 如果用send启动生成器，必须发送非None值
    url = next(gen)
    print(url)
    # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
    html = 'yang'
    print(gen.send(html))
