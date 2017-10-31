#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP,ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/chouti?charset=utf8',max_overflow=5)

Base = declarative_base()

#临时表
class SendCode(Base):
    __tablename__ = 'sendcode'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(32),index=True) #邮箱索引
    stime = Column(TIMESTAMP) #发送验证码时间
    code = Column(String(6))
    status = Column(Integer) #0为注册失败，1为成功，2删除

#创建用户表
class UserInfo(Base):
    __tablename__ = 'userinfo'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(32))
    password = Column(String(32))
    email = Column(String(32))
    ctime = Column(TIMESTAMP)
    status = Column(Integer)  # 0为注册失败，1为成功，2删除

    __table_args__ = (
        Index('ix_user_pwd', 'username', 'password'),
        Index('ix_email_pwd', 'email', 'password'),
    )

def session():
    cls = sessionmaker(bind=engine)

    return cls()
def init_db():
    Base.metadata.create_all(engine)
def drop_db():
    Base.metadata.drop_all(engine)


# drop_db()
# init_db()
