#=============================================================
# File Name: sub_replace.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 05 Jun 2018 04:06:43 PM CST
#=============================================================
# coding:utf8

import re


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# sub() 将pattern匹配到的替换整体替换
# \3 指第3个()里面的值
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

print('\ncompile()预编译')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
