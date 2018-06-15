#=============================================================
# File Name: temp_file.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 15 Jun 2018 05:30:02 PM CST
#=============================================================
# coding:utf8
from tempfile import TemporaryFile


with TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')
    f.seek(0)
    data = f.read()
    print(data)

