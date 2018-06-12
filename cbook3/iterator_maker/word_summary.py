#=============================================================
# File Name: word_summary.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 12 Jun 2018 10:38:25 AM CST
#=============================================================
# coding:utf8
from collections import defaultdict
from itertools import zip_longest


word_summary = defaultdict(list)
with open('somefile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(dict(word_summary))

print('\n---------')
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
# zip() 会创建一个迭代器来作为结果返回。
# 如果你需要将结对的值存储在列表中，要使用 list() 函数
for i in zip_longest(a, b, fillvalue=0):
    print(i)
