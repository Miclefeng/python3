#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/8/1 23:33
#=============================================================
# coding:utf8
from time import sleep, ctime
from multiprocessing import Process, Queue, Pool, Manager, Pipe


# def producer(queue):
#     queue.put("a")
#     sleep(2)
#
# def consumer(queue):
#     sleep(2)
#     data = queue.get()
#     print(data)

def producer(pipe):
    pipe.send("miclefeng")
    sleep(2)

def consumer(pipe):
    sleep(2)
    data = pipe.recv()
    print(data)

def main():
    # 使用Queue进行进程通信
    # 共享全局变量不能适用多进程编程，可适用于多线程
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue, ))
    my_consumer = Process(target=consumer, args=(queue, ))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

if __name__ == '__main__':
    # main()
    # Queue 无法用于进程池pool建立的进程通信
    # 使用Manager中的queue进行通信
    # queue = Manager().Queue(10)
    # pool = Pool(2)
    # pool.apply_async(producer, args=(queue, ))
    # pool.apply_async(consumer, args=(queue, ))
    # pool.close()
    # pool.join()

    # 通过pipe进行进程间通信
    # pipe只能适用于两个进程间的通信
    receive_pipe, send_pipe = Pipe()
    my_producer = Process(target=producer, args=(send_pipe, ))
    my_consumer = Process(target=consumer, args=(receive_pipe, ))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()