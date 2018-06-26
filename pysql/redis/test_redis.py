#=============================================================
# File Name: test_redis.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Sun 24 Jun 2018 02:54:18 AM CST
#=============================================================
# coding:utf8
import redis


class TestString:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_set(self):
        res = self.r.set('user1', 'micle')
        print(res)
        return res

    def test_get(self):
        res = self.r.get('user1')
        print(res)
        return res

    def test_mset(self):
        d = {
            'user2': 'feng',
            'user3': 'miclefeng'
            }
        res = self.r.mset(d)
        print(res)
        return res

    def test_mget(self):
        l = ['user2', 'user3']
        res = self.r.mget(l)
        print(res)
        return res

    def test_del(self):
        self.r.delete('user3')


def main():
    obj = TestString()
    # obj.test_set()
    # res = obj.test_get()
    # res = obj.test_mset()
    res = obj.test_mget()
    print(res)

if __name__ == '__main__':
    main()

