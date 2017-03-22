#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import hashlib
from datetime import datetime

from flask import current_app
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

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
    confirm = db.Column(db.Boolean, default=False)

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

    def general_confirm_token(self, expiration=3000):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"confirm": self.id})

    def confirm_email(self, token):
        """confirm the email"""
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        if data["confirm"] != self.id:
            return False
        self.confirm = True
        db.session.add(self)
        return True

    def general_reset_token(self, expiration=3000):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"reset": self.id})

    def reset_token(self, token, new_password):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        if data["reset"] != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def general_change_email_token(self, new_email, expiration=3000):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"change_mail": self.id, "new_email": new_email})

    def change_mail_token(self, token, new_mail):
        s = Serializer(current_app.config["SECRET_KRY"])
        try:
            data = s.loads(token)
        except:
            return False
        if data["change_mail"] != self.id:
            return False
        self.email = new_mail
        db.session.add(self)
        return True



