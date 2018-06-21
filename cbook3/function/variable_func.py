#=============================================================
# File Name: variable_func.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 21 Jun 2018 04:21:22 PM CST
#=============================================================
# coding:utf8
import html


# *args 是tuple，**kwargs 是dict
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
            name=name,
            attrs=attr_str,
            value=html.escape(value))
    return element

ele = make_element('item', 'Miclefeng', size='large', quantity=6)
print(ele)
ele = make_element('p', '<spam>')
print(ele)
print('\n----------------')

def recv(maxsize, *, block):
    'Receives a message'
    print(maxsize, block)
recv(1024, block=True)
