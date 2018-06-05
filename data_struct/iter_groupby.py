#=============================================================
# File Name: iter_groupby.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 04:48:46 PM CST
#=============================================================
# coding:utf8

rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
       ]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

# groupby() 函数扫描整个序列并且查找连续相同值（或者根据指定 key 函数返回值相同）的元素序列。
# 在每次迭代的时候，它会返回一个值和一个迭代器对象
# 首先要根据指定的字段将数据排序
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
