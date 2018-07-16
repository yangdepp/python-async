# create by 'yang' in 2018/7/8 
__author__ = 'yang'


class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        # 获取父类，并调用__init__方法
        super().__init__()


if __name__ == '__main__':
    b = B()
