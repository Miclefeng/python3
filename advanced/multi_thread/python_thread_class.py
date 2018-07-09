#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/9 20:58
#=============================================================
# coding:utf8
import time, threading


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super(GetDetailHtml, self).__init__(name=name)
    
    def run(self):
        print('get detail html started')
        time.sleep(2)
        print('get detail html end')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super(GetDetailUrl, self).__init__(name=name)

    def run(self):
        print('get detail url started')
        time.sleep(3)
        print('get detail url end')
        with open('test_thread.log', 'wt') as f:
            f.write('this is a test \n')


if __name__ == '__main__':
    thread1 = GetDetailHtml('get_detail_html')
    thread2 = GetDetailUrl('get_detail_url')
    start_time = time.time()
    # 设置守护进程，会和主程序一块退出
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()

    print('last time : {}'.format(time.time() - start_time))
