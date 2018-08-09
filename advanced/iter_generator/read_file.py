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
            # 返回每次buf第一个分隔符前的字符串
            yield buf[:pos]
            # 过滤掉前一个取出的字符串 和 newline
            buf = buf[pos + len(newline):]
        # 每次读取4096个字节
        chunk = f.read(4096)

        # 判断是否到文件末尾
        if not chunk:
            # 文件读完直接返回最后的内容
            yield buf
            break

        # 上一次读取剩下的内容+新读取的内容
        buf += chunk


with open('input.txt') as f:
    for line in myreadlines(f, '{|}'):
        print(line)
