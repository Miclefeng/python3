#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/9 22:54
#=============================================================
# coding:utf8
import time, threading
from queue import Queue


def get_detail_html(queue):
    # 抓取文章详情页
    url = queue.get(1)
    print('get detail html started')
    time.sleep(2)
    print(url)
    print('get detail html end')


def get_detail_url(queue):
    # 爬取文章列表页
    print('get detail url started')
    time.sleep(3)
    for i in range(21):
        queue.put('http://miclefeng.com/{id}'.format(id=i), 1)
    print('get detail url end')

if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=100)
    url_thread = threading.Thread(target=get_detail_url, args=(detail_url_queue, ))

    start_time = time.time()
    threads = []
    for i in range(21):
        t = threading.Thread(target=get_detail_html, args=(detail_url_queue, ))
        threads.append(t)

    url_thread.start()
    for i in range(21):
        threads[i].start()

    url_thread.join()
    for i in range(21):
        threads[i].join()


    print('last time: {}'.format(time.time() - start_time))

