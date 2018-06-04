#=============================================================
# File Name: del_list.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 28 May 2018 04:50:39 PM CST
#=============================================================
# coding:utf8

def dedupe(items, key=None):
    seen = set()
    for item in items:
        print(key(item))
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x':1, 'y':3},{'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
