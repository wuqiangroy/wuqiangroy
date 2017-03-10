#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import render_template, request
from . import auth
from .forms import RegisterForm


@auth.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@auth.route("/register/", methods=["GET", "POST"])
def register():
    """用户注册"""

    form = RegisterForm(request.args)
    if not form.validate():
        """error page"""
    phone_number = form.phone_number.data.replace(" ", "")
    password = form.password.data.replace(" ", "")

    """发送短信"""