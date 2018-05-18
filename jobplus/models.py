# *_*coding:utf-8 *_*

import enum
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class ExperEnum(enum.Enum):
    p_all = 1
    p_one = 2
    p_two = 3

class EduEnum(enum.Enum):
    e_one = "专科"
    e_two = "本科"
    e_three = "硕士"


user_job = db.Table(
    'user_job',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('job_id', db.Integer(), db.ForeignKey('job.id')),
    db.Column('interview_tag', db.Integer()),
    db.Column('c_time', db.DateTime, default=datetime.utcnow),

)


class Base(db.Model):
    c_time = db.Column(db.DateTime, default=datetime.utcnow)
    u_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32))
    pwd = db.Column(db.String(50))
    mobile = db.Column(db.Integer)
    role = db.Column(db.SmallInteger)  # 1 普通用户  2 管理员
    work_year = db.Column(db.SmallInteger)
    resume = db.Column(db.String(50))
    is_Forbidden = db.Column(db.Boolean, default=False)  # False 启用  True 禁用


class Job_info(Base):
    __tablename__ = 'job_info'

    id = db.Column(db.Integer, primary_key=True)
    comp_id = db.Column(db.Integer, db.ForeignKey("company.id", ondelete='CASCADE'))
    job_title = db.Column(db.String(32), nullable=False)
    high_wages = db.Column(db.Integer)
    low_wages = db.Column(db.Integer)
    location = db.Column(db.String(32))
    job_tag = db.Column(db.String(32))
    experience_range = db.Column(db.Enum(ExperEnum)) #!!!!!!!!!!!
    edu_require = db.Column(db.Enum(EduEnum))
    job_desc = db.Column(db.Text)
    is_offline = db.Column(db.Boolean, default=False)  # False 上线  True 下线


class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete='CASCADE'))
    comp_logo = db.Column(db.String(100))
    comp_site = db.Column(db.String(32))
    comp_brief = db.Column(db.String(100))
    comp_location = db.Column(db.String(100))
    comp_detail = db.Column(db.Text)
