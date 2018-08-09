# -*- coding: utf-8
from collections import OrderedDict


# 使用 Python 的 OrderedDict(双向链表 + 字典) 来实现一个简单的 LRU 算法
class LRUDict():

    def __init__(self, capacity):
        self.capacity = capacity
        # OrderedDict 是一个有序的双向链表，会根据插入数据的顺序进行排序
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        old_v = self.items.get(key)

        if old_v is not None:
            # 设置已存在的元素并更新其在字典中的位置
            self.items.pop(key)
            self.items[key] = value
        elif len(self.items) < self.capacity:
            self.items[key] = value
        else:
            # 移除队首元素，即最先放入的元素
            self.items.popitem(last=False)
            self.items[key] = value

    def __getitem__(self, key):
        value = self.items.get(key)

        if value is not None:
            # 访问已存在的元素并更新其在字典中的位置
            self.items.pop(key)
            self.items[key] = value

        return value

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':
    d = LRUDict(10)

    for i in range(10):
        d[i] = i
    print(d)

    for i in range(3):
        print(d[i])
    print(d)

    for i in range(10, 15):
        d[i] = i
    print(d)
