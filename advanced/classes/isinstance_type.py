#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/1 15:21
#=============================================================
# coding:utf8

class A:
    pass


class B(A):
    pass

b = B()
print(isinstance(b, B))
print(isinstance(b, A))
print(id(B))
print(id(A))
print(type(b) is B)
print(type(b) is A)