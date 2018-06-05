#=============================================================
# File Name: re_split.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 05 Jun 2018 10:19:45 AM CST
#=============================================================
# coding:utf8

import re


line = 'asdf fjdk; afed, fjek,asdf, foo'
new_l = re.split(r'[;,\s]\s*', line)
print(new_l)
print("\nre.split 使用捕获分组即使用():")
# 使用了捕获分组，那么被匹配的文本也将出现在结果列表中
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
print("\nre.split 使用?:去除捕获分组:")
print(re.split(r'(?:,|;|\s)\s*', line))

values = fields[::2]
delimiters = fields[1::2] + ['']

print("\nfields[::2] 2代表step")
print(values)
print("\nfields[1::2] 从1开始，step为2")
print(delimiters)
print("\nzip(values, delimiters)")
print(list(zip(values, delimiters)))
print("join v + d")
print(''.join(v + d for v, d in zip(values, delimiters)))
