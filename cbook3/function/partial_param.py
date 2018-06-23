#=============================================================
# File Name: partial_param.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 22 Jun 2018 11:14:30 AM CST
#=============================================================
# coding:utf8
from functools import partial
import math


def spam(a, b, c, d):
    print(a, b, c, d)
# partial() 函数允许你给一个或多个参数设置固定的值
# 减少接下来被调用时的参数个数
s1 = partial(spam, 1)
s1(2, 3, 4)
s2 = partial(spam, 11, 22, d=44)
s2(33)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    # hypot = sqrt(x*x + y*y)
    return math.hypot(x2 - x1, y2 - y1)
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()
