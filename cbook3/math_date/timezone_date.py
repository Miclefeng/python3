#=============================================================
# File Name: timezone_date.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 08 Jun 2018 10:52:09 AM CST
#=============================================================
# coding:utf8

from datetime import datetime
from pytz import timezone


d = datetime(2018, 6, 8, 10, 51, 0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
