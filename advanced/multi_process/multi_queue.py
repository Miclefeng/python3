from multiprocessing import Process, Queue
from time import ctime, sleep
import os, random


def write(q):
    print('Process to Write: {}'.format(os.getpid()))
    for v in ['A', 'B', 'C', 'D']:
        print('Put {} to queue at : '.format(v), ctime())
        q.put(v)
        sleep(random.random())

def read(q):
    print('Process to Read: {}'.format(os.getpid()))
    while True:
        v = q.get(True)
        print('Get {} from queue at: '.format(v), ctime())

def main():
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()

    pw.join()

    pr.terminate()
    print(random.random())

if __name__ == '__main__':
    main()