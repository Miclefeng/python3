#=============================================================
# File Name: str_2_date.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 08 Jun 2018 10:26:29 AM CST
#=============================================================
# coding:utf8

from datetime import datetime


text = '2018-06-08'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(y)
print(z)
print(diff)

nice_z =datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

# parse_ymd 这个函数比 datetime.strptime() 快7倍多
def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))
print(parse_ymd('2018-08-01'))
