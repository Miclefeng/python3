#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/2 0:11
#=============================================================
# coding:utf8

class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()

# super 的执行顺序遵循 MRO
if __name__ == '__main__':
    print(D.__mro__)
    d = D()

# mixin模式特点：
# 1、mixin类功能单一
# 2、不和基类关联，可以和任意基类组合，基类可以不和mixin关联就能初始化
# 3、在mixin中不要使用super()
