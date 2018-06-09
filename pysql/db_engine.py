# =============================================================
# File Name: db_engine.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Sat 09 Jun 2018 10:28:55 AM CST
# =============================================================
# coding:utf8
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
import db_conf as config

engine = create_engine('mysql+pymysql://' + config.USER + ':'
                       + config.PASSWD + '@' + config.HOST + ':' + config.PORT + '/' + config.DB,
                       echo=True)
metadata = MetaData(engine)
Base = declarative_base()

news = Table('news', metadata,
             Column('id', Integer, autoincrement=True, primary_key=True),
             Column('title', String(128), nullable=False, default=''),
             Column('content', String(2048), nullable=False, default=''),
             Column('types', String(12), nullable=False, default=''),
             Column('image', String(256), nullable=False, default=''),
             Column('author', String(24), nullable=False, default=''),
             Column('view_count', Integer, default=0),
             Column('created_at', Integer, default=0),
             Column('id_valid', SmallInteger, default=1))

if __name__ == '__main__':
    metadata.create_all()
