#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/3 22:36
#=============================================================
# coding:utf8
from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('miclefeng', date(year=1992, month=2, day=28))
    user.age = 27
    print(user.age)
    print(user._age)