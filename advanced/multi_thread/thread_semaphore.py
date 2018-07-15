#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/12 23:47
#=============================================================
# coding:utf8
from threading import Thread, Semaphore
from time import ctime, sleep


class HtmlSpider(Thread):
    def __init__(self, url, sem):
        Thread.__init__(self)
        self.url = url
        self.sem = sem

    def run(self):
        sleep(2)
        print('Got html success at: ', ctime())
        # 对semaphore中的值进行递增操作
        self.sem.release()

class UrlProducer(Thread):
    def __init__(self, sem):
        Thread.__init__(self)
        self.sem = sem

    def run(self):
        for i in range(20):
            # 对semaphore中的值进行递减操作
            sem.acquire()
            html_t = HtmlSpider("https://baidu.com/{}".format(i), sem)
            html_t.start()

if __name__ == '__main__':
    sem = Semaphore(5)
    url_producer = UrlProducer(sem)
    url_producer.start()