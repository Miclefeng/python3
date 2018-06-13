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

with open('somefile.txt', 'wt') as f:
    f.write('golang\n')
    f.write('beengo\n')

# 将 print() 函数的输出重定向到一个文件中去
with open('somefile.txt', 'wt') as f:
    print('python', file=f)
    print('flask', file=f)
    print('scrapy', file=f)
