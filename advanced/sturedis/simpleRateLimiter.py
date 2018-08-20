# coding: utf8
import redis
import time


client = redis.StrictRedis()

def is_action_allowed(user_id, action_key, period, max_count):
    key = 'hist:{:s}:{:s}'.format(user_id, action_key)
    now_ts = int(time.time() * 1000)

    with client.pipeline() as pipe:
        pipe.zadd()