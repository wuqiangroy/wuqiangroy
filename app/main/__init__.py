#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint

main = Blueprint("main", __name__)

from .main import views
