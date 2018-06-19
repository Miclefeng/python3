#=============================================================
# File Name: buffer_mmap.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 14 Jun 2018 05:22:01 PM CST
#=============================================================
# coding:utf8
import os
import mmap


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        # readinto() 方法能被用来为预先分配内存的数组填充数据
        # readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回它们
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'hello world')

buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'HELLO'
print(buf)
# memoryview ， 它可以通过零复制的方式对已存在的缓冲区执行切片操作，甚至还能修改它的内容。
m1 = memoryview(buf)
m2 = m1[-5:]
print(bytes(m2))
m2[:] = b'WORLD'
print(buf)
print('\n--------------')

# memeory_map() 函数打开的文件同时支持读和写操作。 任何的修改内容都会复制回原来的文件中。
# 如果需要只读的访问模式，可以给参数 access 赋值为 mmap.ACCESS_READ
# 如果你想在本地修改数据，但是又不想将修改写回到原始文件中，可以使用 mmap.ACCESS_COPY
# 内存映射一个文件并不会导致整个文件被读取到内存中。
# 也就是说，文件并没有被复制到内存缓存或数组中。相反，操作系统仅仅为文件内容保留了一段虚拟内存。
# 当你访问文件的不同区域时，这些区域的内容才根据需要被读取并映射到内存区域中。 而那些从没被访问到的部分还是留在磁盘上
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000
with open('data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
m[0:11] = b'Hello World'
print(m[0:10])
print(m[0])
m.close()

with open('data', 'rb') as f:
    print(f.read(11))
print('\n-----------')
with memory_map('data') as m:
    print(len(m))
    print(m[0:11])
