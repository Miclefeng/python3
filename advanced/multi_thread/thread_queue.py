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
    while True:
        url = queue.get()
        print('get detail html started')
        time.sleep(2)
        print(url)
        print('get detail html end')


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print('get detail url started')
        time.sleep(3)
        for i in range(21):
            queue.put('http://miclefeng.com/{id}'.format(id=i))
        print('get detail url end')

if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=100)
    url_thread = threading.Thread(target=get_detail_url, args=(detail_url_queue, ))
    # url_thread.start()
    for i in range(3):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue, ))
        html_thread.start()

    start_time = time.time()
    detail_url_queue.task_done()
    detail_url_queue.join()

    print('last time: {}'.format(time.time() - start_time))

