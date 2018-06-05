#=============================================================
# File Name: collection_counter.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 04:05:42 PM CST
#=============================================================
# coding:utf8

words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
            'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
            'my', 'eyes', "you're", 'under'
        ]

from collections import Counter

word_counts = Counter(words)

top_three = word_counts.most_common(3)
print(top_three)
print("\n")

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)
print("\n")
# 使用update方法
word_counts.update(morewords)
print(word_counts)
print("\n")

#可以很容易的跟数学运算操作相结合
a = Counter(words)
b = Counter(morewords)
print('a + b 结果为：')
print(a + b)
print("\n")
print('a - b 结果为：')
print(a - b)
