#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/30 0:54
#=============================================================
# coding:utf8
import os
from time import ctime, sleep


def main():
    pid = os.fork()
    # fork copy当前进程，所以会打印两边
    print('miclefeng')

    if pid == 0:
        print('子进程：{}，父进程：{}。'.format(os.getpid(), os.getppid()))
    else:
        print('我是父进程：{}'.format(os.getpid()))
    sleep(2)

if __name__ == '__main__':
    main()