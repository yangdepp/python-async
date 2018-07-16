# create by 'yang' in 2018/7/11 
__author__ = 'yang'
from collections.abc import Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


# 自定义一个迭代器
class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError as e:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['yang', 'deng', 'hahaha'])
    company1 = iter(company)
    while True:
        try:
            print(next(company1))
        except StopIteration:
            pass

