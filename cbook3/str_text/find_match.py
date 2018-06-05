#=============================================================
# File Name: find_match.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 05 Jun 2018 03:36:34 PM CST
#=============================================================
# coding:utf8

import re

text = 'yeah, but no, but yeah, but no, but yeah'
print('text.find(): Search for the location of the first occurrence')
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# 使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
print("\n使用re.compile将pattern预编译为模式对象")
datepat = re.compile(r'\d+/\d+/\d+')
# match() 总是从字符串开始去匹配
if datepat.match(text1):
    print('Yes')
else:
    print('No')

print('\nfindall() 查找字符串任意部分的模式出现位置:')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

print('\nfindall() 方法会搜索文本并以列表形式返回所有的匹配:')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

print('\nfinditer() 以迭代方式返回匹配')
for m in datepat.finditer(text):
    print(m.groups())
