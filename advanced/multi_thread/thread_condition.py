# =============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/12 23:34
# =============================================================
# coding:utf8
from threading import Condition, Thread


class TianMao(Thread):
    def __init__(self, cond):
        Thread.__init__(self, name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{} : 小爱同学'.format(self.name))
            # 通知cond释放condition级别锁
            self.cond.notify()
            # 释放系统锁，并添加一把condition级别的锁
            self.cond.wait()

            print('{} : 我们来对古诗吧'.format(self.name))
            self.cond.notify()
            self.cond.wait()


class XiaoAi(Thread):
    def __init__(self, cond):
        Thread.__init__(self, name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print('{} : 在'.format(self.name))
            self.cond.notify()

            self.cond.wait()
            print('{} : 好的'.format(self.name))
            self.cond.notify()


def main():
    cond = Condition()
    tianmao = TianMao(cond)
    xiaoai = XiaoAi(cond)

    # 在with condition之后才是调用wait和notify方法
    # condition有两层锁，一把是底层锁会在线程调用wait时释放
    # wait在添加一把心锁到deque，notify释放deque中wait添加的锁
    xiaoai.start()
    tianmao.start()

if __name__ == '__main__':
    main()
