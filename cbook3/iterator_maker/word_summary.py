#=============================================================
# File Name: word_summary.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 12 Jun 2018 10:38:25 AM CST
#=============================================================
# coding:utf8
from collections import defaultdict


word_summary = defaultdict(list)
with open('somefile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(dict(word_summary))
