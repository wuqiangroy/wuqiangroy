#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_required
from . import auth
from .forms import RegisterForm, LoginForm
from ..models import User


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


@auth.route("/login/", methods=["GET", "POST"])
def login():
    """user log in"""

    form = LoginForm(request.args)
    if form.validate():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(form.password.data):
            # need session
            return redirect(url_for("main.sweet_grass"))
        flash(u"用户名或密码错误！")
        return redirect(url_for("main.sweet_grass"))
    return render_template("login.html", form=form)


@login_required
@auth.route("/logout/")
def logout():
    """user logout, must be login status"""
    logout_user()
    return redirect(url_for("main.sweet_grass"))