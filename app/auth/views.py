#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_required, login_user, current_user
from . import auth
from .util import send_mail
from .forms import RegisterForm, LoginForm, ChangePwdForm, ForgetPwdForm,\
    ChangeEmailForm
from ..models import User


@auth.route("/register/", methods=["GET", "POST"])
def register():
    """用户注册"""

    form = RegisterForm(request.args)
    if form.validate():
        user = User(
            username=form.username.data,
            email=form.email.data,
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

        token = user.general_reset_token()
        send_mail(user.email, u"更改密码",
                  "auth/email/change_pwd", user=user, token=token)
        flash(u"一封确认邮件已经发送，请注意查收！")
    return render_template("auth/change_password.html", form=form)


@auth.route("/forget-password/", methods=["GET", "POST"])
def forget_password():
    """user forgets password, and can reset password"""

    form = ForgetPwdForm(request.args)
    if form.validate():
        user1 = User.query.filter_by(username=form.username.data).first()
        user2 = User.query.filter_by(email=form.email.data).first()
        if not user1:
            flash(u"用户不存在！")
            return redirect(url_for("auth.forget_password"))
        if not user2:
            flash(u"非注册邮箱！")
            return redirect(url_for("auth.forget_password"))
        if user1 != user2:
            flash(u"用户名和邮箱不匹配！")
            return redirect(url_for("auth.forget_password"))
        token = user1.general_reset_token()
        send_mail(form.email.data, u"重置密码",
                  "auth/email/forget_pwd", user=user1, token=token)
        flash(u"一封确认邮件已经发送，请注意查收！")
    return render_template("auth/forget_password.html", form=form)


@login_required
@auth.route("/change-email/", methods=["GET", "POST"])
def change_email():
    """
    user can change email,
    only need to click the url in the email by sended
    """

    form = ChangeEmailForm(request.args)
    if form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            new_email = form.new_email.data
            token = user.general_change_email_token(new_email)
            send_mail(new_email, u"更换邮箱",
                      "auth/email/change_email", user=user, token=token)
            flash(u"一封确认邮件已经发送，请注意查收！")
        flash(u"用户名或密码错误！")
        return redirect(url_for("auth.change_mail"))
    return render_template("auth/change_email.html", form=form)
