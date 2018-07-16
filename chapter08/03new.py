# create by 'yang' in 2018/7/10 
__author__ = 'yang'


class User:
    # 允许在user对象之前加逻辑
    # 传递的是类
    def __new__(cls, *args, **kwargs):
        print('in new')
        # 如果new方法不返回对象，则不会调用init函数
        return super().__new__(cls)

    # 传递的是实例化的对象
    def __init__(self, name):
        print('in init')
        self.name = name


if __name__ == '__main__':
    user = User('yang')
