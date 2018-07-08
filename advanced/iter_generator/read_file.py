#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/7 1:26
#=============================================================
# coding:utf8

def myreadlines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            # 获取分隔符所在的位置
            pos = buf.index(newline)
            # 返回分隔符第一段数据
            yield buf[:pos]
            # 剔除上一次分割出的第一段数据
            buf = buf[pos + len(newline):]
        # 每次读取4096个字节
        chunk = f.read(4096)

        # 判断是否到文件末尾
        if not chunk:
            yield buf
            break
        buf += chunk


with open('input.txt') as f:
    for line in myreadlines(f, '{|}'):
        print(line)
