#=============================================================
# File Name: date_friday.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 05:05:32 PM CST
#=============================================================
# coding:utf8
from datetime import datetime, timedelta


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']

# 获取上一周某天的日期
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    print('获取开始日期的星期数')
    print(day_num)
    print(start_date)
    day_num_target = weekdays.index(dayname)
    print('\n获取目标星期数')
    print(day_num_target)
    days_ago = (7 + day_num - day_num_target)
    print('\n获取两个星期之间的差值')
    print(days_ago)
    if 0 == days_ago:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

lastweekF = get_previous_byday('Friday')
print('\n上周五日期')
print(lastweekF)
print('\n---------------')
lastweekM = get_previous_byday('Monday')
print('\n上周一日期')
print(lastweekM)
