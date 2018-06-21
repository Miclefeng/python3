#=============================================================
# File Name: struct_encode.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 21 Jun 2018 11:24:08 AM CST
#=============================================================
# coding:utf8
from struct import Struct
from collections import namedtuple


def write_records(records, format, f):
    '''
    将一系列元组写入结构的二进制文件。
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# 增量读取文件中的数据
def read_records(format, f):
    record_struct = Struct(format)
    # 生成迭代对象，但不执行f.read，文件指针位于初始位置
    # 这个迭代器会不断的调用一个用户提供的可调用对象(比如 lambda: f.read(record_struct.size) )，
    # 直到它返回一个特殊的值(如b'')，这时候迭代停止
    chunks = iter(lambda: f.read(record_struct.size), b'')
    # f.read 读取size个字节，文件指针移动到size处
    # chunk = f.read(record_struct.size)
    # print(record_struct.unpack(chunk))
    # print('\n-------------')
    # 遍历迭代对象，f.read执行，读取size之后的数据
    # unpack 读取的是每一段偏移的数据
    return (record_struct.unpack(chunk) for chunk in chunks)

def unpack_records(format, data):
    record_struct = Struct(format)
    # unpack_from() 从一个大型二进制数组中提取二进制数据时不会产生临时对象或者进行内存复制操作
    # 在原数据上读取，参数为二进制数据和读取的偏移量
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))

if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
            (6, 7.8, 9.0),
            (12, 13.4, 56.7)]
    with open('data.b', 'wb') as f:
        # i, d, f等分别代表特定的二进制数据类型
        # 32位整数，64位浮点数，32位浮点数
        write_records(records, '<idd', f)

    with open('data.b', 'rb') as f:
       for res in read_records('<idd', f):
           print(res)

    print('\n---------------')
    with open('data.b', 'rb') as f:
        data = f.read()
        for res in unpack_records('<idd', data):
            print(res)

    print('\n---------------')
    Record = namedtuple('Record', ['kind', 'x', 'y'])
    with open('data.b', 'rb') as f:
        records = (Record(*r) for r in read_records('<idd', f))
        for r in records:
            print(r.kind, r.x, r.y)
