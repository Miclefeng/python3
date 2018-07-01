#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/1 23:38
#=============================================================
# coding:utf8
from advanced.classes.class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1992, 2, 28))
    print(user._User__birthday)
    print(User.__birthday)
    print(user.get_age())