#=============================================================
# File Name: format_vars.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Wed 06 Jun 2018 04:18:53 PM CST
#=============================================================
# coding:utf8

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Miclefeng', 26)
# 如果要被替换的变量能在变量域中找到， 那么你可以结合使用 format_map() 和 vars()
print('\nvars(a) 获取对象实例的变量域,使用format_map匹配替换')
print(s.format_map(vars(a)))

import sys

# 处理缺失的变量使用 __missing__ 方法
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

# sys._getframe(1) 返回调用者的栈帧。可以从中访问属性 f_locals 来获得局部变量。
# f_locals 是一个复制调用函数的本地变量的字典
def usub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Miclefengzss'
n = 26
print(usub('Hello {name}'))
print(usub('I`am {n}'))
print(usub('Your favorite color is {color}'))
