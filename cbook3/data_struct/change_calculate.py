#=============================================================
# File Name: change_calculate.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 06:32:57 PM CST
#=============================================================
# coding:utf8

import os

files = os.listdir('/opt/python/base/python3/data_struct')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
print("\n")
portfolio = [
                {'name':'GOOG', 'shares': 50},
                {'name':'YHOO', 'shares': 75},
                {'name':'AOL', 'shares': 20},
                {'name':'SCOX', 'shares': 65}
            ]

min_shares = min(s['shares'] for s in portfolio)
max_shares = max(portfolio, key=lambda s: s['shares'])
print(min_shares)
print(max_shares)
