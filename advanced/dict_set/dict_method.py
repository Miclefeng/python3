#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/3 0:23
#=============================================================
# coding:utf8
a = {'micle': {'address': 'beijing'},
     'striveftf': {'address': 'taian'}}

# copy，浅拷贝，值为原来的引用
# new_dict = a.copy()
# new_dict['micle']['address'] = 'bj'
# print('a is : ', a)
# print('new_dict is : ', new_dict)

new_list = ['Aquarius', 'imooc']
new_dict = dict.fromkeys(new_list, {'address': 'taian'})
# {'Aquarius': {'address': 'taian'}, 'imooc': {'address': 'taian'}}
print(new_dict)
print('\n')

import copy
new_dict = copy.deepcopy(a)
new_dict['micle']['address'] = 'bj'
print('a is : ', a)
print('new_dict is : ', new_dict)

new_dict.update([('aquarius', {'address': 'taian'})])
print('\n')
print(new_dict)