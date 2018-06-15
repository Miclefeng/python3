#=============================================================
# File Name: listdir_glob.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 15 Jun 2018 03:42:20 PM CST
#=============================================================
# coding:utf8
import os
import glob
from fnmatch import fnmatch


names = [name for name in os.listdir('/opt/python/base/python3')
        if os.path.isfile(
            os.path.join('/opt/python/base/python3', name))]
print('Filename:')
print(names)

dirnames = [name for name in os.listdir('/opt/python/base/python3')
        if os.path.isdir(
            os.path.join('/opt/python/base/python3', name))]
print('\nDirname:')
print(dirnames)

pyfiles = glob.glob('/opt/python/base/python3/cbook3/file_io/*.py')
print(pyfiles)

pyfiles = [name for name in os.listdir('/opt/python/base/python3/cbook3/file_io') if fnmatch(name, '*.py')]
print(pyfiles)
print('\n-------------')
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
