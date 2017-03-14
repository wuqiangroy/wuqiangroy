#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""配置"""

import os
import sys


class Config(object):
    """base config"""
    SECRET_KEY = os.environ.get("secret_key") or "easy to guess secret key"
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = "smtp-mail.outlook.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DATABASE_SETTING = {
        "username": os.environ.get("username"),
        "password": os.environ.get("password")
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """development config, based on Config"""
    DEBUG = True

    username = Config.DATABASE_SETTING["username"]
    password = Config.DATABASE_SETTING["password"]

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_UIR") or \
        "mysql://{0}:{1}@localhost:3306/dev_wuqiangroy".format(username,
                                                               password)


class TestingConfig(Config):
    """testing config, based on Config"""

    TESTING = True

    username = Config.DATABASE_SETTING["username"]
    password = Config.DATABASE_SETTING["password"]

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_UIR") or \
        "mysql://{0}:{1}@localhost:3306/testing".format(username,
                                                        password)

    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):

    username = Config.DATABASE_SETTING["username"]
    password = Config.DATABASE_SETTING["password"]

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_UIR") or \
        "mysql://{0},{1}@localhost:3306/wuqiangroy".format(username,
                                                           password)

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

