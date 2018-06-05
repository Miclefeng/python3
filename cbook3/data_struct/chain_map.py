#=============================================================
# File Name: chain_map.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 05 Jun 2018 09:51:48 AM CST
#=============================================================
# coding:utf8

from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print("\n x, z, y")
# ChainMap 类只是在内部创建了一个容纳这些字典的列表
# 并重新定义了一些常见的字典操作来遍历这个列表
# 如果出现重复键，那么第一次出现的映射值会被返回
print(list(c.values()))

