#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/26 18:52
#=============================================================
# coding:utf8
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor


# 对于cpu密集型，使用多进程
# 对于IO密集型，使用多线程
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)

def multi_process():
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, num) for num in range(25, 35)]
        print('Process Start as: ', time.ctime())
        for future in as_completed(all_task):
            data = future.result()
            print('Get Result is {}'.format(data))
        print('Process Finish as: ', time.ctime())

def multi_thread():
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25, 35)]
        print('Thread Start at: ', time.ctime())
        for future in as_completed(all_task):
            data = future.result()
            print('Get Result is {}'.format(data))
        print('Thread Finished at: ', time.ctime())

def main():
    multi_thread()
    multi_process()

if __name__ == '__main__':
    main()