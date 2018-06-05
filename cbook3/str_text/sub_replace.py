#=============================================================
# File Name: sub_replace.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 05 Jun 2018 04:06:43 PM CST
#=============================================================
# coding:utf8

import re
from calendar import month_abbr


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# sub() 将pattern匹配到的替换整体替换
# \3 指第3个()里面的值
# flags=re.IGNORECASE 忽略大小写
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text, flags=re.IGNORECASE))

print('\ncompile()预编译')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

print('\nmonth_abbr[10]:')
print(month_abbr[10])
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
# 类似PHP preg_replace_callback() + preg_replace
print('\n使用自定义函数进行替换')
#替换回调函数的参数是一个 match 对象，也就是 match() 或者 find() 返回的对象
print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print('\nsubn() 返回 替换后的结果 和 替换次数')
print(newtext, n)
