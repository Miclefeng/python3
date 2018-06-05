#=============================================================
# File Name: obj_sorted.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Mon 04 Jun 2018 04:30:42 PM CST
#=============================================================
# coding:utf8

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
def sort_notcompare():
    print(users)
    print("\nOrder by lambda:")
    print(sorted(users, key=lambda u: u.user_id))

sort_notcompare()

from operator import attrgetter
print("\nOrder by attrgetter:")
print(sorted(users, key=attrgetter('user_id')))
