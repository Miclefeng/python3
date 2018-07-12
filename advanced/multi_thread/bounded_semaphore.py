#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/12 22:39
#=============================================================
# coding:utf8
from atexit import register
from threading import Lock, BoundedSemaphore, Thread
from time import ctime, sleep
from random import randrange


lock = Lock()
MAX = 5
# 信号量实例
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('Refilling candy...')
    try:
        # 增加信号量的计数器资源
        candytray.release()
    except:
        print('Full, skipping')
    else:
        print('Ok')
    print('Refill candytray len: ', candytray.__dict__['_value'])
    lock.release()

def buy():
    lock.acquire()
    print('Buying candytray')
    # 释放信号量的计数器资源
    if candytray.acquire(False):
        print('Ok')
    else:
        print('Empty, skipping')
    print('Buy candytray len: ', candytray.__dict__['_value'])
    lock.release()

def producer(loops):
    for x in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for x in range(loops):
        buy()
        sleep(randrange(3))

def main():
    print('Starting at: ', ctime())
    nloops = randrange(2, 6)
    print(nloops)
    print('The Candy Machine (full with {:d} bars!)'.format(MAX))
    Thread(target=consumer, args=(nloops, )).start()
    Thread(target=producer, args=(nloops, )).start()

@register
def _atexit():
    print('All Done at: ', ctime())

if __name__ == '__main__':
    main()


