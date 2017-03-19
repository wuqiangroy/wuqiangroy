#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_required, login_user, current_user
from . import auth
from .util import send_mail
from .forms import RegisterForm, LoginForm, ChangePwdForm
from ..models import User


@auth.route("/register/", methods=["GET", "POST"])
def register():
    """用户注册"""

    form = RegisterForm(request.args)
    if form.validate():
        user = User(
            username=form.username.data.replace(" ", ""),
            email=form.email.data.replace(" ", ""),
            password=form.password.data
        )
        token = user.general_confirm_token()
        send_mail(user.email, u"确认您的账户",
                  "auth/email/confirm", user=user, token=token)
        return render_template("auth.email_confirm")
    return render_template("auth/register.html", form=form)


@auth.route("/email-confirm/", methods=["GET", "POST"])
def email_confirm():
    """waiting page"""
    # waiting 5 seconds automatic


@auth.route("/login/", methods=["GET", "POST"])
def login():
    """user log in"""

    form = LoginForm(request.args)
    if form.validate():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("main.sweet_grass"))
        flash(u"用户名或密码错误！")
        return redirect(url_for("main.sweet_grass"))
    return render_template("login.html", form=form)


@login_required
@auth.route("/logout/")
def logout():
    """user logout, must be login status"""
    logout_user()
    flash(u"你已经退出了！")
    return redirect(url_for("main.sweet_grass"))


@login_required
@auth.route("/change-password/", methods=["GET", "POST"])
def change_password():
    """user can change password"""

    form = ChangePwdForm(request.args)
    user = User.query.filter_by(email=current_user.email).first()
    if form.validate():
        password = form.password.data
        if not user.verify_password(password):
            flash(u"密码错误！请重新输入")
            return redirect(url_for("auth.change_password"))

        token = user.general_confirm_token(expiration=3600)
        send_mail(user.email, u"更改密码",
                  "auth/email/change_pwd", user=user, token=token)
    return render_template("auth/change_password.html", form=form)


@auth.route("/forget-password/", methods=["GET", "POST"])
def forget_password():
    """user forgets password, and can reset password"""
    pass
