# create by 'yang' in 2018/7/8 
__author__ = 'yang'

import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print('file open')
    yield {}
    print('file end')


with file_open('nnn') as f_opened:
    print('file processing')
