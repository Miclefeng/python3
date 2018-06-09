#=============================================================
# File Name: test_con_search.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Sat 09 Jun 2018 03:13:36 PM CST
#=============================================================
# coding:utf8
import pymysql
import db_conf as config


class MysqlSearch():
    def __init__(self):
        self.get_con()

    def get_con(self):
        try:
            self.con = pymysql.connect(
                host = config.HOST,
                user = config.USER,
                password = config.PASSWD,
                database = config.DB,
                use_unicode = True,
                charset = 'utf8')
            self.cursor = self.con.cursor()
        except Exception as e:
            print(e)

    def get_one(self):
        sql = 'SELECT * FROM `news` WHERE `types`=%s ORDER BY `id` DESC;'
        self.cursor.execute(sql, ('百家', ))
        res = dict(zip([k[0] for k in self.cursor.description], self.cursor.fetchone()))
        self.close_con()
        return res

    def get_more(self):
        sql = 'SELECT * FROM `news` WHERE `types`=%s ORDER BY `id` DESC;'
        self.cursor.execute(sql, ('百家', ))
        res = [dict(zip([k[0] for k in self.cursor.description], row)) for row in self.cursor.fetchall()]
        self.close_con()
        return res

    def get_more_by_page(self, page = 1, page_size = 10):
        page = page if page else 1
        page_size = page_size if page_size else 10
        print(page, page_size)
        offset = (page - 1) * page_size
        sql = 'SELECT * FROM `news` WHERE `types`=%s ORDER BY `id` DESC LIMIT %s,%s;'
        self.cursor.execute(sql, ('百家', offset, page_size))
        res = [dict(zip([k[0] for k in self.cursor.description], row)) for row in self.cursor.fetchall()]
        self.close_con()
        return res

    def add_one(self):
        try:
            sql = ("INSERT INTO `news` (`title`, `author`, `image`,`content`,`types`,`is_valid`,`created_at`)"
                "VALUES"
                "(%s, %s, %s, %s, %s, %s, %s)")
            self.cursor.execute(sql, ('标题6666', '', '/static/img/news/06.png', '新闻内容66666', '推荐', 1, 1528534194))
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print(e)
        self.close_con()

    def close_con(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()
        except Exception as e:
            print(e)

def main():
    obj = MysqlSearch()
    # res = obj.get_one()
    # print(res)
    # res = obj.get_more_by_page(0, 0)
    # res = obj.get_more()
    # for item in res:
    #    print(item)
    #    print('------------------')
    # obj.add_one()

if __name__ == '__main__':
    main()
