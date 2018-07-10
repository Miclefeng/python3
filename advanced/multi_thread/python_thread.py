#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/9 0:35
#=============================================================
# coding:utf8
import threading
import time


def get_detail_html(url):
    print('get html detail start')
    time.sleep(2)
    print('get detail html end')

def get_detail_url(url):
    print('get detail url start')
    time.sleep(4)
    print('get detail url end')

if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=('', ))
    thread2 = threading.Thread(target=get_detail_url, args=('', ))
    start_time = time.time()
    # 设置为守护线程，表示这个线程是不重要的，进程退出时不需要等待这个线程
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()

    # 阻塞主线程直到子线程完成
    thread1.join()
    thread2.join()
    # 当主线程退出时，子线程kill掉
    print('last time: {}'.format(time.time() - start_time))