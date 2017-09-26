#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/zuoye?charset=utf8')
Base = declarative_base()

#创建成绩表
class Score(Base):
    __tablename__ = 'score'
    sid = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey('student.sid'))
    course_id = Column(Integer,ForeignKey('course.cid'))
    number= Column(Integer)

# 创建班级表
class Class(Base):
    __tablename__ = 'class'
    cid = Column(Integer, primary_key=True)
    caption = Column(String(32))


# 创建学生表
class Student(Base):
    __tablename__ = 'student'
    sid = Column(Integer, primary_key=True)
    sname = Column(String(32))
    gender = Column(String(32))
    class_id = Column(Integer, ForeignKey('class.cid'))
    s_class = relationship('Class', backref='c_student')
    course_list = relationship('Course',secondary=Score.__table__, backref='student_list')

#创建老师表
class Teacher(Base):
    __tablename__ = 'teacher'
    tid = Column(Integer, primary_key=True)
    tname = Column(String(32))
    t_course = relationship('Course', backref='c_teacher')

#创建课程表
class Course(Base):
    __tablename__ = 'course'
    cid = Column(Integer, primary_key=True)
    cname = Column(String(32))
    teacher_id = Column(Integer, ForeignKey('teacher.tid'))



def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

# init_db()

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    c1= Class(caption='三年二班')
    c2= Class(caption='一年三班')
    c3= Class(caption='三年一班')
    s1=Student(sname='钢蛋',gender='女',class_id=1)
    s2=Student(sname='铁锤',gender='女',class_id=1)
    s3=Student(sname='山炮',gender='男',class_id=2)
    session.add_all([c1,c2,c3])
    session.commit()
    session.add_all([s1,s2,s3])
    session.commit()
    t1=Teacher(tname='波多')
    t2=Teacher(tname='苍井')
    t3=Teacher(tname='饭岛')
    cu1=Course(cname='生物')
    cu2=Course(cname='体育')
    cu3=Course(cname='物理')
    t1.t_course=[cu1,cu2]
    t2.t_course=[cu3]
    session.add_all([t1,t2,t3])
    session.commit()
    so1=Score(student_id=1,course_id=1,number=60)
    so2=Score(student_id=1,course_id=2,number=59)
    so3=Score(student_id=2,course_id=2,number=100)
    session.add_all([so1,so2,so3])
    session.commit()

