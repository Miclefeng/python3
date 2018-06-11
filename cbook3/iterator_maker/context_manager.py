#=============================================================
# File Name: context_manager.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 11 Jun 2018 10:22:31 PM CST
#=============================================================
# coding:utf8
from contextlib import contextmanager


class MyResource:
    def query(self):
        print('query data')

@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection!')

@contextmanager
def book_mark():
    print('《', end='')
    yield
    print('》', end='')

if __name__ == '__main__':
    with make_myresource() as r:
        r.query()

    with book_mark():
        print('奇点临近', end='')
