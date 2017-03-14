#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

mail = Mail()
login_manager = LoginManager()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)
    from .main import main
    app.register_blueprint(main)
