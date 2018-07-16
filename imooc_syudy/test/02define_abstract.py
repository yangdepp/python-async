# create by 'yang' in 2018/7/12 
__author__ = 'yang'

# 定义并使用一个抽象基类
import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        '''从迭代对象中添加元素'''

    @abc.abstractmethod
    def pick(self):
        '''
            随机删除元素，然后将其返回
            如果实例为空，这个方法应该抛出'LookupError'
        '''

    def loaded(self):
        '''如果至少有一个元素，返回True，否则返回False'''
        return bool(self.inspect())

    def inspect(self):
        pass