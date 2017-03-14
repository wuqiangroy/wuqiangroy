#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import hashlib
from datetime import datetime

from werkzeug.security import generate_password_hash,check_password_hash

from app import db


"""db"""


class Permission:
    pass


class Goods(db.Modle):
    __tablename__ = "goods"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    category = db.Column(db.String(64))
    pic = db.Column(db.String(256))
    introduction = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Role(db.Model):
    """user's role including permission etc"""
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permission = db.Column(db.Integer)


class User(db.Model):
    """user's db including name, phone number etc"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("warning: you can not catch password!")

    # hash password, do not stored express password
    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    # verify the input password vs hashed password
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)



