#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/1 15:23
#=============================================================
# coding:utf8

class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 类变量所有实例共享
a = A(2, 3)
# 实例变量，实例单独拥有
print(a.x, a.y, a.aa)
print(A.aa)