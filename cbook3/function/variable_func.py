#=============================================================
# File Name: variable_func.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 21 Jun 2018 04:21:22 PM CST
#=============================================================
# coding:utf8
import html


# lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，
# 函数的默认值参数定义是在函数定义是绑定
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10), b(10))
print('\n-------------')
# 运行时绑定值，n 的值都绑定为4
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))
print('----------')
# n=n 是黄参数的值定义为默认参数
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))
print('\n-----------')

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

def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print('\n')
print(mininum(1, 5, -2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))

