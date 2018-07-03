#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/3 22:44
#=============================================================
# coding:utf8
from datetime import date


class User:
    def __init__(self, info={}):
        self.info = info

    # 访问一个不存在的属性时调用
    def __getattr__(self, item):
        return self.info[item]

    # 访问属性时就会调用
    # def __getattribute__(self, item):
    #     return item

if __name__ == '__main__':
    user = User(info={'name': 'miclefeng', 'birthday': date(year=1992, month=3, day=31), 'company_name': 'imooc'})
    print(user.name)
    print(user.birthday)
    print(user.company_name)
    print(user.test)