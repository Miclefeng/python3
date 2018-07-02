#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/2 22:53
#=============================================================
# coding:utf8
import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice) or isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

    def __str__(self):
        return ', '.join(self.staffs)


if __name__ == '__main__':
    staffs = ['micle', 'miclefeng', 'imooc', 'python']
    group = Group(company_name='imooc', group_name='user', staffs=staffs)
    print(len(group))
    sub_group = group[:2]
    print(sub_group)
    sub_group = group[0]
    print(sub_group)
    reversed(group)
    for item in group:
        print(item)
    if 'micle' in group:
        print('Yes')
# 4
# micle, miclefeng
# m, i, c, l, e
# python
# imooc
# miclefeng
# micle
# Yes
