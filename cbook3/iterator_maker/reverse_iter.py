#=============================================================
# File Name: yield_iter.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 08 Jun 2018 03:20:40 PM CST
#=============================================================
# coding:utf8

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))

# yield 语句即可将其转换为一个生成器。 跟普通函数不同的是，生成器只能用于迭代操作
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

print('\n')
c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c, None))

class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 反向迭代
    # 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(CountDown(10)):
    print(rr)
print('\n-------------')
for rr in CountDown(10):
    print(rr)






