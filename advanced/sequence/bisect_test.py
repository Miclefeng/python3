#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/2 23:06
#=============================================================
# coding:utf8
import bisect


# 用来处理已排序的序列，用来维持已排序的序列， 升序
# 使用二分查找实现
inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 6)

# bisect = bisect_right
print(bisect.bisect(inter_list, 4))
print(bisect.bisect_left(inter_list, 4))
print(inter_list)
