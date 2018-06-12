#=============================================================
# File Name: is_iterable.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 12 Jun 2018 03:52:41 PM CST
#=============================================================
# coding:utf8
from collections import Iterable


def flttern(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flttern(x)
            # yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用。
            # 如果你不使用它的话，那么就必须写额外的for 循环了。
            # for i in flttern(x):
            #    yield i
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flttern(items):
    print(x)
