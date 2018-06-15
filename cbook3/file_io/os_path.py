#=============================================================
# File Name: os_path.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 14 Jun 2018 06:08:50 PM CST
#=============================================================
# coding:utf8
import os
import time


path = '/opt/python/base/python3/cbook3/file_io/somefile.txt'
base_name = os.path.basename(path)
print(base_name)
dir_name = os.path.dirname(path)
print(dir_name)
print('\nos.path.join:')
print(os.path.join('tmp', 'data', base_name))
print('\nos.path.expanduser:')
print(os.path.expanduser('~/arr.php'))
print('\nos.path.splitext:')
print(os.path.splitext(path))
print('\nos.path.exists:')
print(os.path.exists('/etc/passwd'))
print('\nos.path.isfile | isdir | islink')
print(os.path.isfile('/etc/passwd'))
print('\nos.path.realpath:')
print(os.path.realpath('/usr/bin/python'))
print('\nos.path.getsize:')
print(os.path.getsize('/etc/passwd'))
print('\nos.path.getmtime:')
print(os.path.getmtime('/etc/passwd'))
print(time.ctime(os.path.getmtime('/etc/passwd')))
