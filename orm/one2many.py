#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/orm')
Base = declarative_base()  # 生成一个Base基类


# 创建表，继承基类
class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    age = Column(String(32))
    father_id = Column(Integer, ForeignKey('father.id'))


class Father(Base):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    age = Column(String(32))

    # def __repr__(self):
    #     return self.name


# 执行创建表
def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


init_db()

# 建立插入数据连接
Session = sessionmaker(bind=engine)
session = Session()

f1 = Father(name='cuicui1', age=64)
f2 = Father(name='cuicui2', age=44)
f3 = Father(name="cuicui3", age=24)

# 增加数据
session.add(f1)
session.add_all([f2,f3])
session.commit()
# ret = session.query(Father).all() #ret是father表中的每一行，是个对象
# ret_first = session.query(Father).first() #ret是father表中的第一行也是个对象
# print(session.query(Father)) #SELECT father.id AS father_id, father.name AS father_name, father.age AS father_age FROM father
# print(ret) #[<__main__.Father object at 0x000001705ADF6588>, <__main__.Father object at 0x000001705ADF65F8>, <__main__.Father object at 0x000001705ADF6668>]
# for i in ret:
#     print(i.name,i.age)
# print(ret_first.name)

s1= Son(name='little cuicui1',age=1,father_id=1)
s2= Son(name='little cuicui2',age=1,father_id=1)
s3= Son(name='little cuicui3',age=1,father_id=2)
session.add_all([s1,s2,s3])
session.commit()
# ret = session.query(Father.name,Father.age).join(Son).all()
# ret = session.query(Father.name,Father.age,Son.name.label('s_name')).join(Son).all()
# print(ret)

# print(session.query(Father).filter(Father.id.in_([1,2])).all())
