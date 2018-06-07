#=============================================================
# File Name: randoms.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 02:56:13 PM CST
#=============================================================
# coding:utf8

import random


values = [1, 2, 3, 4, 5, 6]
print(values)
print('\nrandom.choice():')
print(random.choice(values))
print(random.choice(values))
print('\nrandom.sample():')
print(random.sample(values, 2))
print(random.sample(values, 2))
print('\nrandom.shuffle():')
random.shuffle(values)
print(values)
print('\nrandom.ranint():')
print(random.randint(0, 10))
print('\nrandom.random():')
# 生成0到1范围内均匀分布的浮点数
print(random.random())

