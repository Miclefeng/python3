# =============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/7 1:26
# =============================================================
# coding:utf8

def myreadlines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096)

        if not chunk:
            yield buf
            break
        buf += chunk


with open('input.txt') as f:
    for line in myreadlines(f, '{|}'):
        print(line)