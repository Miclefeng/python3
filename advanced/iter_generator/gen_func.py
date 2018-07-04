#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/5 1:41
#=============================================================
# coding:utf8

def fib(idx):
    if idx <= 2:
        return 1
    else:
        return fib(idx - 2) + fib(idx - 1)


def gen_fib(idx):
    n, a, b = 0, 0, 1
    while n < idx:
        yield b
        a, b = b, a + b
        n += 1

if __name__ == '__main__':
    print(fib(10))
    for v in gen_fib(10):
        print(v, end='\t')