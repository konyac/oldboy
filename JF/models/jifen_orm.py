#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP,DATE, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/jifen?charset=utf8', max_overflow=5)

Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password = Column(String(32))


# 创建用户表
class UserInfo(Base):
    __tablename__ = 'userinfo'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password = Column(String(32))
    name = Column(String(32))
    sex = Column(String(32))
    birth = Column(DATE)
    inout = Column(Integer)
    id = Column(String(32))
    department_id = Column(Integer, ForeignKey('department.nid'))
    position_id = Column(Integer, ForeignKey('position.nid'))
    __table_args__ = (
        Index('ix_user_pwd', 'username', 'password'),
    )


#
class Department(Base):
    __tablename__ = 'department'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))


#
class Position(Base):
    __tablename__ = 'position'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    # inout_id = Column(Integer) #本部机构
    pofl_id = Column(Integer, ForeignKey('position_fl.nid'))  # 岗位分类
    name = Column(String(128))
    inout = Column(Integer)


class Position_fl(Base):
    __tablename__ = 'position_fl'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))



#
class Item(Base):
    __tablename__ = 'item'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    fl_id = Column(Integer, ForeignKey('fenlei.nid'))
    ej_id = Column(Integer, ForeignKey('erji.nid'))
    name = Column(String(1024))
    # fenlei = relationship("fenlei", backref='item')
    # erji = relationship("erji", backref='item')


class Fenlei(Base):
    __tablename__ = 'fenlei'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(32))


class Erji(Base):
    __tablename__ = 'erji'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    Ename = Column(String(32))


class zhibiao(Base):
    __tablename__ = 'zhibiao'

    nid = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey('item.nid'))
    Zname = Column(String(1024))
    # item = relationship("item", backref='zhibiao')


class Upload(Base):
    __tablename__ = 'upload'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('userinfo.nid'))
    value = Column(Integer)
    status = Column(Integer)
    ctime = Column(TIMESTAMP)
    item_id = Column(Integer, ForeignKey('item.nid'))
    zhibiao_id = Column(Integer, ForeignKey('zhibiao.nid'))
    content = Column(String(1024))


#
# class News(Base):
#
#     __tablename__ = 'news'
#     nid = Column(Integer,primary_key=True,autoincrement=True)
#     user_info_id = Column(Integer,ForeignKey('userinfo.nid'))
#     news_type_id = Column(Integer,ForeignKey('newstype.nid'))
#     ctime = Column(TIMESTAMP)
#     title = Column(String(32))
#     url = Column(String(128))
#     content = Column(String(150))
#     favor_count = Column(Integer, default=0)#点赞个数
#     comment_count = Column(Integer, default=0)#评论格式
#     f = relationship('Favor', backref='n')
#
# class Favor(Base):
#
#     __tablename__ = 'favor'
#
#     nid = Column(Integer, primary_key=True, autoincrement=True)
#     user_info_id = Column(Integer, ForeignKey("userinfo.nid"))
#     news_id = Column(Integer, ForeignKey("news.nid"))
#     ctime = Column(TIMESTAMP)
#
#     __table_args__ = (
#         UniqueConstraint('user_info_id', 'news_id', name='uix_uid_nid'),
#     )
#
# class Comment(Base):
#
#     __tablename__ = 'comment'
#
#     nid = Column(Integer, primary_key=True, autoincrement=True)
#     user_info_id = Column(Integer, ForeignKey("userinfo.nid"))
#     news_id = Column(Integer, ForeignKey("news.nid"))
#     reply_id = Column(Integer, ForeignKey("comment.nid"), nullable=True, default=None)
#     up = Column(Integer)
#     down = Column(Integer)
#     ctime = Column(TIMESTAMP)
#     device = Column(String(32))
#     content = Column(String(150))

def session():
    cls = sessionmaker(bind=engine)

    return cls()


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    drop_db()
    init_db()
