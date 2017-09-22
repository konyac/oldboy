#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/orm2')
Base = declarative_base()  # 生成一个Base基类


class Men_to_Wemon(Base):
    __tablename__ = 'men_to_wemon'
    nid = Column(Integer, primary_key=True)
    men_id = Column(Integer, ForeignKey('men.id'))
    women_id = Column(Integer, ForeignKey('women.id'))


class Men(Base):
    __tablename__ = 'men'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    # gf= relationship("Women", secondary=Men_to_Wemon.__table__)


class Women(Base):
    __tablename__ = 'women'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    bf = relationship("Men", secondary=Men_to_Wemon.__table__, backref='gf')  # backref='gf' 相当于在men类定义了gf字段
Base.metadata.create_all(engine)

