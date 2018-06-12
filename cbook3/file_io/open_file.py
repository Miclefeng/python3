#=============================================================
# File Name: open_file.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 12 Jun 2018 06:23:40 PM CST
#=============================================================
# coding:utf8

with open('somefile.txt', 'rt') as f:
    # data = f.read()
    # print(data)
    for line in f:
        print(line)
