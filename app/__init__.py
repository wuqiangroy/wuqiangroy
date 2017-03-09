#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask


def create_app():
    app = Flask(__name__)

    from .auth import auth
    app.register_blueprint(auth)
