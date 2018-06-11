#=============================================================
# File Name: itertools_skip.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 11 Jun 2018 04:21:57 PM CST
#=============================================================
# coding:utf8
from itertools import islice, dropwhile


with open('/etc/passwd') as f:
    # 跳过可迭代对象的开始部分
    # itertools.dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。
    # 它会返回一个迭代器对象，丢弃原有序列中直到函数返回Flase之前的所有元素，然后返回后面所有元素。
    for line in dropwhile(lambda line: line.startswith('root'), f):
        print(line, end='')
    # 过滤以nobody开始的行
    # lines = (line for line in f if not line.startswith('nobody'))
    # for line in lines:
    #    print(line, end='')

# 函数 dropwhile() 和 islice() 其实就是两个帮助函数,可以同下面函数实现一样的功能
with open('/etc/passwd') as f:
    while True:
        line = next(f, '')
        if not line.startswith('root'):
            break

    while line:
        print(line, end='')
        line = next(f, None)

items = ['a', 'b', 'c', 1, 4, 10, 15]
# islice() 函数最后那个 None 参数指定了你要获取从第3个到最后的所有元素，
# 如果 None和3的位置对调，意思就是仅仅获取前三个元素恰恰相反
# 这个跟切片的相反操作 [3:] 和 [:3] 原理是一样的。
for x in islice(items, 3, None):
    print(x)
