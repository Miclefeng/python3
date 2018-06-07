#=============================================================
# File Name: date_time.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 03:22:54 PM CST
#=============================================================
# coding:utf8
from datetime import timedelta
from datetime import datetime


a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))
