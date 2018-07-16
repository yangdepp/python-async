# create by 'yang' in 2018/7/8 
__author__ = 'yang'


def exe_try():
    try:
        print('code start')
        raise KeyError
        return 1
    except KeyError as e:
        print('key error')
        return 2
    else:
        print('else error')  # 没有抛异常才能运行到else
        return 3
    finally:
        print('finally error')  # 不管有没有都执行，一般用作资源的释放
        return 4  # 注释掉会返回2


if __name__ == '__main__':
    result = exe_try()
    print(result)

print('-' * 50)


# 上下文管理器，with语法简化try
class Smple:
    def __enter__(self):
        # 获取资源
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print('exit')

    def do_something(self):
        print('do something')


with Smple() as smple:
    smple.do_something()
