#=============================================================
# File Name: priority_queue.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 28 May 2018 03:31:58 PM CST
#=============================================================
# coding:utf8
import heapq


class PriorityQueue:
    _queue = []
    _index = 0

    @classmethod
    def push(cls, item, priority):
        #使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。
        #但是如果两个元素优先级一样的话，那么比较操作就会出错
        #引入另外的 index 变量组成三元组 (priority, index, item))
        #使 index 的值累加，元组前两个元素就可以排序，后续元素就不会进行比较
        heapq.heappush(cls._queue, (-priority, cls._index, item))
        cls._index += 1

    @classmethod
    def pop(cls):
        # heappop 返回队列中最小的元素
        return heapq.heappop(cls._queue)[-1]

    def getQueue(self):
        print(sorted(self._queue))

class Item:
    def __init__(self, name):
        self.name = name

    # __repr__ 和 __str__ 类似 PHP 中魔术方法 __toString()
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
# Python 在做元组比较时候，如果前面的比较已经可以确定结果了， 后面的比较操作就不会发生了
# a < b = True |  a < c = True

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

q.getQueue()
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
