#=============================================================
# File Name: combinations_iter.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 11 Jun 2018 05:49:42 PM CST
#=============================================================
# coding:utf8
from itertools import permutations, combinations, combinations_with_replacement


items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)
print('\n---------------')

for p in permutations(items, 2):
    print(p)
print('\n---------------')

# 对于 combinations() 来讲，元素的顺序已经不重要了
for p in combinations(items, 3):
    print(p)
print('\n---------------')
for p in combinations(items, 2):
    print(p)
print('\n---------------')
for p in combinations(items, 1):
    print(p)
print('\n---------------')

# 函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次
for c in combinations_with_replacement(items, 3):
    print(c)
