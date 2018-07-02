#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/2 21:31
#=============================================================
# coding:utf8
from collections import abc

a = [1, 2]
# + 只接收list类型
c = a + [3, 4]
# += 接收任意类型, 实际调用extend()
a += [3, 4]
a += (5, 6)
print(a)
print(c)
# 将每一个元素追加到列表中
a.extend(range(4))
print(a)
# 将整个元素追加到列表中
a.append([7, 8])
print(a)
a.append((7, 8))
print(a)