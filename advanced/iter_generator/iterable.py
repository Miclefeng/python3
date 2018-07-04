#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/4 23:54
#=============================================================
# coding:utf8
from collections.abc import Iterator


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代器的逻辑
        try:
            data = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return data


if __name__ == '__main__':
    com = Company(['micle', 'miclfeng', 'striveftf'])

    for item in com:
        print(item)