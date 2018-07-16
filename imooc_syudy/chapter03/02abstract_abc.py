# 抽象基类 abc模块
from collections import Sized
import abc


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['1', '2'])
if hasattr(com, '__len__'):
    print(len(com))

# 在某些情况之下，希望判定某个对象的类型
if isinstance(com, Sized):
    print('hello')


# 需要强制某个子类必须实现某些方法
# 设计一个抽象基类，指定子类必须实现某些方法
# 如何去模拟一个抽象基类

# 模拟一个抽象基类
# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#
#
# class RedisCache(CacheBase):
#     pass
#
#
# redis_cache = RedisCache()
# redis_cache.set('key', 'value')
# print('hel')

# 全局模块下的abc
class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


# 继承的时候，必须实现get 和set方法，不然在初始化的时候就会抛异常
class RedisCache(CacheBase):
    pass


# 实例化时会报错
redis_cache = RedisCache()
