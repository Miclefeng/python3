#=============================================================
# File Name: test_con_orm.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Sun 10 Jun 2018 04:27:34 PM CST
#=============================================================
# coding:utf8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Boolean
import db_conf as config


engine = create_engine('mysql://' + config.USER + ':' + config.PASSWD + '@'
        + config.HOST + ':' + config.PORT  + '/' + config.DB)
Base = declarative_base()


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    content = Column(String(2048), nullable=False)
    types = Column(String(12), nullable=False)
    image = Column(String(256), )
    author = Column(String(32), )
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

# News.metadata.create_all(engine)
