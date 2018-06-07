#=============================================================
# File Name: get_fib.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 10:21:16 AM CST
#=============================================================
# coding:utf8

def get_fib(n):
    if 0 == n:
        return 0

    if 1 == n:
        return 1

    res = get_fib(n - 1) + get_fib(n - 2)
    return res

print(get_fib(4))
print(get_fib(5))
print(get_fib(6))
print(get_fib(7))
