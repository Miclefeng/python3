#=============================================================
# File Name: serialize.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 15 Jun 2018 05:47:49 PM CST
#=============================================================
# coding:utf8
import pickle


f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4, 5], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()
