#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from wtforms import Form, StringField, IntegerField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, equal_to


class RegisterForm(Form):
    """用户注册表单"""
    phone_number = IntegerField(u"手机号", validators=[DataRequired(), Length(1, 11)])
    password = PasswordField(u"密码", validators=[DataRequired()])
    submit = SubmitField(u"注册")


class UserForm(Form):
    """用户详情表单"""
    username = StringField(u"昵称", validators=[DataRequired(), Length(1, 30)])
    about_me = StringField(u"一句话描述", validators=[Length(1, 100)])
    email = StringField(u"邮箱", validators=[Email()])
