#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/31 0:32
#=============================================================
# coding:utf8
import multiprocessing
from time import ctime, sleep


def get_html(n):
    sleep(n)
    print('sub_process success')
    return n

def main():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3, ))
    # pool.close()
    # pool.join()
    # print(result.get())

    # for result in pool.imap(get_html, [1, 3, 2, 4]):
    #     print('{} sleep success'.format(result))

    for result in pool.imap_unordered(get_html, [1, 3, 2, 4]):
        print('{} sleep success'.format(result))

if __name__ == '__main__':
    main()