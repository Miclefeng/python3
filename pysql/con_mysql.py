#=============================================================
# File Name: con_mysql.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 07 Jun 2018 12:41:32 AM CST
#=============================================================
# coding:utf8
import pymysql


class MysqlOpt:
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        """获取连接"""
        try:
            self.conn = pymysql.connect(
                        host='127.0.0.1',
                        user='',
                        passwd='',
                        db='',
                        port=3306,
                        charset='utf8'
                    )
        except pymysql.Error as e:
            print('Error %d: %s' % (e.args[0], e.args[1]))

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error %d: %s' % (e.args[0], e.args[1]))

    def get_one(self):
        sql = 'SELECT * FROM `user` WHERE `id`=%s;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('3', ))
        res = cursor.fetchone()
        print(res)
        cursor.close()
        self.close_conn()

def main():
    obj = MysqlOpt()
    obj.get_one()

if __name__ == '__main__':
    main()
