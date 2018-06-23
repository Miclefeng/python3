#=============================================================
# File Name: extra_func.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 22 Jun 2018 04:00:32 PM CST
#=============================================================
# coding:utf8

def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def print_result(result):
    print('Got: ', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('Hello', 'World'), callback=r.handler)
print('\n--------------')

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('Hello', 'World'), callback=handler.send)
