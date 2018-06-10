#=============================================================
# File Name: test_con_mysql.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Sat 09 Jun 2018 11:38:52 AM CST
#=============================================================
# coding:utf8
import pymysql
import db_conf as config


# 获取数据库连接
conn = pymysql.connect(
            host = config.HOST,
            user = config.USER,
            password = config.PASSWD,
            database = config.DB,
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor)

# 获取游标
cursor = conn.cursor()
try:
    # 执行SQL
    cursor.execute('SELECT * FROM `news` ORDER BY `id` DESC;')
    res = cursor.fetchone()
    print(res)
except Exception as e:
    print(e)
finally:
    # 关闭游标和数据库连接
    cursor.close()
    conn.close()




