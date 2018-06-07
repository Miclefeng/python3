#=============================================================
# File Name: decimal_calculate.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 11:01:09 AM CST
#=============================================================
# coding:utf8

from decimal import Decimal
from decimal import localcontext
import math


a = Decimal('4.2')
b = Decimal('2.1')

print(a + b)
print((a + b) == Decimal('6.3'))

c =Decimal('1.7')
d = Decimal('1.3')
print(d / c)
with localcontext() as ctx:
    ctx.prec = 3
    print(d / c)

with localcontext() as ctx:
    ctx.prec = 9
    print(d / c)

nums = [1.23e+18, 1, -1.23e+18]
print(math.fsum(nums))

