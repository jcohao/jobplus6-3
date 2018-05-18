# *_*coding:utf-8 *_*

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column()
    passwd = db.Column()
    mobile = db.Column()
    c_time


class Employee(db.Model):
    pass


class Company(db.Model):
    pass
