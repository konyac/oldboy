#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/orm3?charset=utf8')
Base = declarative_base()  # 生成一个Base基类


class HostToGroup(Base):
    __tablename__ = 'host_2_group'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    Group_id = Column(Integer, ForeignKey('group.id'))


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)
    group = relationship('Group', secondary=HostToGroup.__table__, backref='host_list')


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    # host_list=relationship('Host' ,secondary=HostToGroup.__table__,)

    def __repr__(self):
        return "<id=%s,name=%s>" % (self.id, self.name)


Base.metadata.create_all(engine)  # 创建表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    # 插入数据第一种方式
    # g1 = Group(name='g1')
    # g2 = Group(name='g2')
    # g3 = Group(name='g3')
    # g4 = Group(name='g4')
    # session.add_all([g1, g2, g3, g4])
    # h1 = Host(hostname='h1', ip_addr='192.168.1.56')
    # h2 = Host(hostname='h2', ip_addr='192.168.1.57', port=10000)
    # h3 = Host(hostname='ubuntu', ip_addr='192.168.1.58', port=10000)
    # session.add_all([h1, h2, h3])
    # session.commit()

    groups = session.query(Group).all()
    h2 = session.query(Host).filter(Host.hostname=='h2').first()
    h2.group = groups[:-1]#取前三个，一台主机绑定3个组
    print("===========>",h2.group)

    g4 = session.query(Group).filter(Group.name == 'g4').first()
    print(g4)
    obj1 = session.query(Host).filter(Host.hostname == 'h1').update({'port': 444})#改值

    h2= session.query(Host).filter(Host.hostname == 'h1').first()

    g4.host_list.append(h2)
    # h2.group.append(g4)
    session.commit()