#=============================================================
# File Name: join_str.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 06 Jun 2018 02:27:17 PM CST
#=============================================================
# coding:utf8

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

with open('filename', 'w') as fp:
    for part in combine(sample(), 32768):
        fp.write(part)
