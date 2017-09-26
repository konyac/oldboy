#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/orm3?charset=utf8')
Base = declarative_base()  # 生成一个Base基类


class Men_to_Women(Base):
    __tablename__ = 'men_to_women'
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
    bf = relationship("Men", secondary=Men_to_Women.__table__, backref='gf')
    # backref='gf' 相当于在men类定义了gf字段
    #secondary 用来对应第三张表的。


# 创建表
# Base.metadata.create_all(engine)  # 3 在数据库生成表
# 删除表
# Base.metadata.drop_all(engine) # 3 在数据库生成表

Session = sessionmaker(bind=engine)
session = Session()
# 第一种 插入数据

# 数据汉字报错。。。。未,charset=utf8
# m1 = Men(name='alex', age=18)
# m2 = Men(name='xx', age=18)
# w1 = Women(name='铁锤', age=40)
# w2 = Women(name='钢蛋', age=45)
# session.add_all([m1, m2, w1, w2, ])
# session.commit()
# t1 = Men_to_Women(men_id=1, women_id=2)  # 插入关系
# session.add(t1)
# session.commit()

# 第二种 插入数据
m1 = session.query(Men).filter_by(id=2).first()  # 查询id为2的男人
print(m1)
w1 = session.query(Women).all()  # 查询所有女人 为列表对象
m1.gf = w1  # 设置绑定关系 2号男跟所有女人 此时关系表2号还没绑定 如果2好已经有关系绑定。这里也不是所有women 只是某一个元素的话,就需要是m1.gf.append(w1)了,如果w1是一个列表的话就要m1.gf.extend(w1)了

session.add_all([m1, ])  # 参考一对多 中的。
session.commit()
