#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/1 14:28
#=============================================================
# coding:utf8
from collections.abc import Sized
import abc


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(['micle', 'miclefeng'])
print(hasattr(com, '__len__'))

# 使用抽象基类
# 1、在某些情况之下判定某个对象的类型
print(isinstance(com, Sized))

# 2、强制某个子类必须实现某些方法
# example：实现一个web框架，集成cache(sturedis, cache, file)
# 需要设计一个抽象基类，指定子类必须实现某些方法


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass

redis_cache = RedisCache()
redis_cache.set('k', 'v')