#=============================================================
# File Name: open_file.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Tue 12 Jun 2018 06:23:40 PM CST
#=============================================================
# coding:utf8
import array
from functools import partial


with open('somefile.txt', 'rt') as f:
    # data = f.read()
    # print(data)
    for line in f:
        print(line)

with open('somefile.txt', 'wt') as f:
    f.write('golang\n')
    f.write('beengo\n')

# 将 print() 函数的输出重定向到一个文件中去
with open('somefile.txt', 'wt') as f:
    print('python', file=f)
    print('flask', file=f)
    print('scrapy', file=f)

nums = array.array('i', [1, 2, 3, 4])
#with open('data.bin', 'wb') as f:
#    f.write(nums)

with open('data.bin', 'wb') as f:
    f.write('this is a test miclefengzss brightdh admin python flask scrapy high skills sql'.encode('utf-8'))

RECORD_SIZE = 32
with open('data.bin', 'rb') as f:
    # iter()如果你给它传递一个可调用对象和一个标记值，它会创建一个迭代器。
    # 这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止
    # functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象。 标记值 b''
    # 就是当到达文件结尾时的返回值
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
