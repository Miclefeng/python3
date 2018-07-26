#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/15 13:02
#=============================================================
# coding:utf8
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED, Future
from time import ctime, sleep


# Future 未来对象，task的返回容器



# 线程池
#1、主线程获取某一个线程、任务的状态以及返回值
#2、子线程完成时通知主线程
#3、futures可以让多线程和多进程编程的接口一致

def get_html(nsec):
    print('Got page {} at: {}'.format(nsec, ctime()))
    sleep(nsec)
    return nsec

def main():
    executor = ThreadPoolExecutor(max_workers=3)

    # 通过submit提交执行的函数到线程池，submit是立即返回
    # task1 = executor.submit(get_html, 1)
    # task2 = executor.submit(get_html, 2)
    #
    # print(task1.done())
    # sleep(2)
    # print(task1.done())
    urls = [3, 2, 1, 4]
    all_task = [executor.submit(get_html, url) for url in urls]

    # 等待子线程完成在进行后续执行
    wait(all_task, return_when=FIRST_COMPLETED)
    print('First Thread Completed......')

    # 哪个进程先完成就先处理哪个
    for future in as_completed(all_task):
        data = future.result()
        print('PAGE{} SUCCESS At: '.format(data), ctime())

    # 处理顺序与urls中的元素顺序一致
    # for data in executor.map(get_html, urls):
    #     print('PAGE{} SUCCESS At: '.format(data), ctime())


if __name__ == '__main__':
    main()
