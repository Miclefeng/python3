#=============================================================
# File Name: date_range.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 05:41:14 PM CST
#=============================================================
# coding:utf8
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        # replace() 方法简单的将 days 属性设置成1
        start_date = date.today().replace(day=1)
    # monthrange() 函数会返回包含星期和该月天数的元组。
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

first_day, last_day = get_month_range()
print(first_day, last_day)

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2018, 5, 28), datetime(2018, 6, 7), timedelta(hours=12)):
    print(d)
