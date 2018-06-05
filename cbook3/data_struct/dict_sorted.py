#=============================================================
# File Name: dict_sorted.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 04:22:50 PM CST
#=============================================================
# coding:utf8

rows = [
            {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
            {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
            {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
       ]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print('Order by fname: ')
print(rows_by_fname)
print("\nOrder by uid: ")
print(rows_by_uid)
print("\nOrder by lambda lname fname:")
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_lfname)
