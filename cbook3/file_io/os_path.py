#=============================================================
# File Name: os_path.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 14 Jun 2018 06:08:50 PM CST
#=============================================================
# coding:utf8
import os


path = '/opt/python/base/python3/cbook3/file_io/somefile.txt'
base_name = os.path.basename(path)
print(base_name)
dir_name = os.path.dirname(path)
print(dir_name)
print(os.path.join('tmp', 'data', base_name))
print(os.path.expanduser('~/arr.php'))
print(os.path.splitext(path))
