#=============================================================
# File Name: dict_xml.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 20 Jun 2018 06:31:51 PM CST
#=============================================================
# coding:utf8
from xml.sax.saxutils import escape, unescape


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key, val))
    parts.append('<{}>'.format(tag))
    return ''.join(parts)

s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(e)
