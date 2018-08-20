# coding: utf8
import redis
import time


client = redis.StrictRedis()

def is_action_allowed(user_id, action_key, period, max_count):
    key = 'hist:{:s}:{:s}'.format(user_id, action_key)
    now_ts = int(time.time() * 10000)

    with client.pipeline() as pipe:
        pipe.set(key + '_lock', True, nx=True, ex=5)

        # 保证value的值的唯一性
        pipe.zadd(key, now_ts, now_ts)

        # 保留窗口之内的数据，删除超过限流时间的数据
        # 0_15_30_45_60_75_90, 30_45_60_75_90 删除窗口之外的数据，保留限流时间段内的数据
        pipe.zremrangebyscore(key, 0, now_ts - period * 10000)

        # 查询当前窗口的数据大小
        pipe.zcard(key)

        # 设置过期时间，避免冷数据占用内存
        pipe.expire(key, period + 1)
        pipe.delete(key + '_lock')
        _, _, _, current_count, _, _ = pipe.execute()
        print(current_count, now_ts)
    return current_count <= max_count

if __name__ == '__main__':
    for i in range(30):
        time.sleep(1)
        res = is_action_allowed('miclefeng', 'reply', 60, 10)
        print(res)
