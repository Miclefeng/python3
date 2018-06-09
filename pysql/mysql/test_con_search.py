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
    obj.get_one()

if __name__ == '__main__':
    main()
