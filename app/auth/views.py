#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import render_template, request
from . import auth
from .forms import RegisterForm


@auth.route("/register/", methods=["GET", "POST"])
def register():
    """用户注册"""

    form = RegisterForm(request.args)
    if not form.validate():
        """error page"""
    username = form.username.data.replace(" ", "")
    email = form.email.data.replace(" ", "")
    password = form.password.data.replace(" ", "")
    password2 = form.password2.data.replace(" ", "")

    """发送邮件"""