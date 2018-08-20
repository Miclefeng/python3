# -*- coding: utf-8
import time
# import redis


funnels = {}

class Funnel:
    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity # 漏斗容量
        self.leaking_rate = leaking_rate # 漏斗流水速率
        self.left_quota = capacity # 漏斗剩余空间
        self.leaking_ts = time.time() # 上一次流水时间

    def make_space(self):
        now_ts = time.time()
        delta_ts = now_ts - self.leaking_ts # 距离上一次漏水过去多久
        delta_quota = delta_ts * self.leaking_rate # 漏水腾出多少空间
        if delta_quota < 1:
            return False

        self.left_quota += delta_quota # 剩余空间+腾出空间
        if self.left_quota + delta_quota > self.capacity:
            # 漏斗的最大容量
            self.left_quota = self.capacity

        self.leaking_ts = now_ts # 本次漏水时间

    def watering(self, quota):
        self.make_space()
        # 单次需要的空间
        if self.left_quota >= quota:
            # 校验漏斗的剩余空间
            self.left_quota -= quota
            return True
        return False

def is_action_allowed(user_id, action_key, capacity, leaking_rate):
    key = '{:s}:{:s}'.format(user_id, action_key)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)

if __name__ == '__main__':
    for i in range(20):
        print(i, is_action_allowed('miclefeng', 'striveftf', 15, 0.5), time.ctime())
