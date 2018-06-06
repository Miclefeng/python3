#=============================================================
# File Name: format_center.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 06 Jun 2018 11:06:55 AM CST
#=============================================================
# coding:utf8

text = 'Hello World'
print(text.center(20))
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '*^20'))
print(format(text, '=^20'))
print(format(text, '=>20'))
# 6 是填充的6个字符
print('{:|>6s} {:|>8s}'.format('hello', 'world'))
