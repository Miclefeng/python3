#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/10 21:12
#=============================================================
# coding:utf8
import threading
from time import ctime, sleep


loops = [4, 2]

def loop(nloop, nsec):
    print('start loop ', nloop, ' at: ', ctime())
    sleep(nsec)
    print('loop', nloop, ' done at: ', ctime())

def main():
    print('starting at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        # 等待所有线程执行完成
        threads[i].join()

    print('all DONE at: ', ctime())

if __name__ == '__main__':
    main()
