#=============================================================
# File Name: start_endwith.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 05 Jun 2018 11:58:58 AM CST
#=============================================================
# coding:utf8

from urllib.request import urlopen


filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
print("endswith, startswith 参数需要是 str 或者 tuple 类型")
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# print(str(read_data('http://www.baidu.com'), encoding='utf-8'))
# print(read_data('./re_split.py'))
