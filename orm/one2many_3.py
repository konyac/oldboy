#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/orm2')
Base = declarative_base()  # 生成一个Base基类


class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))  # 创建普通索引index=True
    age = Column(String(32))  # 创建唯一索引 唯一不为空可以为null unique=True
    father_id = Column(Integer, ForeignKey("father.id"))
        # “多”的一方的son表是通过外键关联到father表的:


    # def __repr__(self):  # 打印对象的时候,就调用这里 ,我们可以直接打印对象
    #     # 只能return 字符串
    #     return self.name+str(self.age)


class Father(Base):
    __tablename__ = "father"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32))
    age = Column(String(32))
    son = relationship("Son", backref='father')  # 适合第二种插入数据的一对多方式 没有这条的话就需要按照第一种方式插入一对多数据

    # def __repr__(self): #打印对象的时候,就调用这里 ,我们可以直接打印对象
    #     #只能return 字符串
    #     return self.name + str(self.age)


# 1 创建 删除 表
# Base.metadata.create_all(engine)  # 创建两个表
# Base.metadata.drop_all(engine) # 删除两个表


# 2 插入数据

# #这两行触发sessionmaker类下的__call__方法，return得到 Session实例，赋给变量session，所以session可以调用Session类下的add，add_all等方法
# 建立连接
Session = sessionmaker(bind=engine)
session = Session()

# f3 = Father(name="cuicui", age=18)
#
# w1 = Son(name="little cui 5", age=2, )
# w2 = Son(name="little cui 6", age=3, )
# w3 = Son(name="little cui w3", age=3, )

#第一种添加方式
'''
f3.son=[w1,w2]
session.add_all([f3,w1,w2])
session.commit()
'''

# 第二种添加方式
'''
f3.son=[w1,w2]  # son的relationship作用 如果是已经有 w1 w2 对象就需要f3.son
# 如果已经创建过关系,再次添加新的关系就要 f3.son.append(w3) 不然重新赋值 到这原来的 w1 w2 为null了关系

session.add_all([f3])  # 两种添加都行
session.commit()
'''
ret = session.query(Father).filter_by(name='cuicui').first()
for i in ret.son:
    print(i.name)
ret2 = session.query(Son).filter_by(age=3).first()
print(ret2.father.name)
ret3=session.query(Father).filter_by(name='cuicui2').first()
# ret3.son.append(w3)
print(ret3.son)
for i in ret3.son:
    print(i.name)

f2 = Father(name='cuicui2',age=24)
'''
f2.son=[w3]
session.add(f2)
session.commit()
'''


