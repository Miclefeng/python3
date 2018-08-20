# coding: utf8
import redis
import time


client = redis.StrictRedis()

def is_action_allowed(user_id, action_key, period, max_count):
    key = 'hist:{:s}:{:s}'.format(user_id, action_key)
    now_ts = int(time.time() * 10000)

    with client.pipeline() as pipe:
        pipe.set(key + '_lock', True, nx=True, ex=5)
        pipe.zadd(key, now_ts, now_ts)
        pipe.zremrangebyscore(key, 0, now_ts - period * 10000)
        pipe.zcard(key)
        pipe.expire(key, period + 1)
        pipe.delete(key + '_lock')
        _, _, _, current_count, _, _ = pipe.execute()
        print(current_count, now_ts)
    return current_count <= max_count

if __name__ == '__main__':
    for i in range(20):
        res = is_action_allowed('miclefeng', 'reply', 60, 10)
        print(res)
