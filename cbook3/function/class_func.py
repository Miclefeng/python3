#=============================================================
# File Name: class_func.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 22 Jun 2018 02:38:21 PM CST
#=============================================================
# coding:utf8
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,APPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

print('\n--------------')

# 使用闭包函数来代替只有一个类方法的类
def urltemplate(template):
    def opener(**kwargs):
        return template.format_map(kwargs)
    return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,APPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
