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
