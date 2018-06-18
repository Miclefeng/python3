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
from sqlalchemy.orm import sessionmaker
import db_conf as config


engine = create_engine('mysql+pymysql://' + config.USER + ':' + config.PASSWD + '@'
        + config.HOST + ':' + config.PORT  + '/' + config.DB + '?charset=utf8mb4')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    content = Column(String(2048), nullable=False)
    types = Column(String(12), nullable=False)
    image = Column(String(256), default='')
    author = Column(String(32), default='')
    view_count = Column(Integer, default=1)
    created_at = Column(DateTime, )
    is_valid = Column(Boolean, default=True)


class OrmTest:
    def __init__(self):
        self.session = Session()

    def add_one(self):
        try:
            new_obj = News(
                    title='标题2',
                    content='内容2',
                    types='百家',
                    author='miclefengzss')
            self.session.add(new_obj)
            self.session.commit()
            return new_obj
        except:
            self.session.rollback()

    def get_one(self):
        return self.session.query(News).get(1)

    def get_more(self):
        return self.session.query(News).filter_by(is_valid=True)

    def update_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    def delete_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()


def main():
    obj = OrmTest()
    # res = obj.add_one()
    # res = obj.get_one()
    res = obj.get_more()
    if res:
        print('ID:{} => {}'.format(res[0].id, res[0].title))
        print(res.count())
    else:
        print('Not exist.')
    # obj.update_data(1)

if __name__ == '__main__':
    main()
# News.metadata.create_all(engine)
