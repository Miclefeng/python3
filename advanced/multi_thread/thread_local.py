# -*- coding: utf-8

import redis
import threading

# 全局变量locks就是一个ThreadLocal对象，每个Thread对它都可以读写redis属性，但互不影响。
# 你可以把locks看成全局变量，但每个属性如local_school.redis都是线程的局部变量，使得每个线程之间的变量可以任意读写而互不干扰
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

locks = threading.local()
locks.redis = {}


def key_for(user_id):
    return 'account_{}'.format(user_id)

def _lock(client, key):
    return bool(client.set(key, True, nx=True, ex=5))

def _unlock(client, key):
    return bool(client.delete(key))

def lock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] += 1
        return True
    ok = _lock(client, key)
    if not ok:
        return False
    locks.redis[key] = 1
    return True

def unlock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] -= 1
        if locks.redis[key] <= 0:
            del locks.redis[key]
            _unlock(client, key)
        return True
    return False

def main():
    client = redis.StrictRedis()
    print('lock ', lock(client, 'miclefeng'))
    print('lock ', lock(client, 'miclefeng'))
    print('unlock ', unlock(client, 'miclefeng'))
    print('unlock ', unlock(client, 'miclefeng'))

if __name__ == '__main__':
    main()