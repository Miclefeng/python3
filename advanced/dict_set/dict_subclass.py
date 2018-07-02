#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/3 0:32
#=============================================================
# coding:utf8

class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)
my_dict['one'] = 1
print(my_dict)
print('\n')


from collections import UserDict, defaultdict


class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)
my_dict['one'] = 1
print(my_dict)

my_dict = defaultdict(dict)
my_value = my_dict['aquarius']


