#=============================================================
# File Name: filter_element.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 05:46:45 PM CST
#=============================================================
# coding:utf8

mylist = [1, 3, -5, 10, -7, 2, -1, 4]
new = [n for n in mylist if n > 0]
print(new)
print("\nFilter int list:")

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

#将不符合条件的值用新的值代替
# [n if n > 0 else 0 for n in mylist]
# [1, 4, 0, 10, 0, 2, 3, 0]
