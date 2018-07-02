#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/2 23:43
#=============================================================
# coding:utf8
# 列表生成式(列表推导式)
odd_list = []
for i in range(21):
    if 1 == i % 2:
        odd_list.append(i)
print(odd_list)
odd_list = [i for i in range(21) if 1 == i % 2]
print(odd_list)
def handle_item(item):
    return item * item
odd_list = [handle_item(i) for i in range(21) if 1 == i % 2]
print(odd_list)

# 字典推导式
my_dict = {'miclefeng': 23, 'striveftf': 26, 'aquarius': 28}
reversed_dict = {v: k for k, v in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = {k for k, v in my_dict.items()}
print(type(my_set))
print(set(my_dict.keys()))
print(my_set)