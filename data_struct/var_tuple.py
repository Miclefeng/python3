#=============================================================
# File Name: var_tuple.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 28 May 2018 11:20:59 AM CST
#=============================================================
# coding:utf8
from functools import reduce


records = [
        ('foo', 1, 2),
        ('bar', 'hello miclefeng'),
        ('foo', 3, 4)
        ]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

items = [1, 10, 4, 7, 9, 5]
def sum(items):
    head, *tail = items
    #if tail:
    #    return head + sum(tail)
    #else:
    #    return head
    #return head + sum(tail) if tail else head
print(sum(items))

total = reduce(lambda x, y: x + y, items)
print(total)
