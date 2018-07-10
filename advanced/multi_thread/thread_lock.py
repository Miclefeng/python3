#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/11 0:22
#=============================================================
# coding:utf8
from atexit import register
from threading import Thread, Lock, current_thread
from time import ctime, sleep
from random import randrange


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(4, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = current_thread().name
    lock.acquire()
    remaining.add(myname)
    print('[{:s}] Started {:s}'.format(ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[{:s}] Completed {:s} ({:d} secs)'.format(ctime(), myname, nsec))
    print('    (remaining: {%s}' % (remaining or 'NONE'))
    lock.release()

def main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
    print('all DONE at: ', ctime())

if __name__ == '__main__':
    main()
