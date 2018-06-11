#=============================================================
# File Name: linehistory_iter.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 11 Jun 2018 02:53:02 PM CST
#=============================================================
# coding:utf8
from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    with open('somefile.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{} : {}'.format(lineno, hline), end='')

    print('\n------------')
    with open('somefile.txt') as f:
        lines = linehistory(f)
        it = iter(lines)
        print(next(it))
        print(next(it))
        print(next(it))
        print(next(it, None))
