#=============================================================
# File Name: test_mongo.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Sat 23 Jun 2018 07:18:38 PM CST
#=============================================================
# coding:utf8
from pymongo import MongoClient
from datetime import datetime


class TestMongo:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def add_one(self):
        '''
            新增数据
        '''
        post = {
                'title': '新的标题',
                'content': '博客的内容....',
                'view_count': 1,
                'create_at': datetime.now()
                }
        return self.db.blog.posts.insert_one(post)


def main():
    obj = TestMongo()
    res = obj.add_one()
    print(res.inserted_id)

if __name__ == '__main__':
    main()
