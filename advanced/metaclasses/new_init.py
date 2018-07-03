#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/4 0:24
#=============================================================
# coding:utf8
class User:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    def __init__(self, name):
        print('in init')


# new 是用来控制对象的生成过程，在对象生成之前
# init 是用来完善对象
# 如果 new 方法不返回对象，则不会调用 init 函数
if __name__ == '__main__':
    user = User(name='miclefeng')