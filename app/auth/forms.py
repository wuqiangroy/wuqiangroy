#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from wtforms import Form, StringField, IntegerField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, equal_to, Regexp


class LoginForm(Form):
    """user login form"""

    username = StringField(u"用户名", validators=[DataRequired()])
    password = PasswordField(u"密码", validators=[DataRequired()])
    submit = SubmitField(u"登陆")


class RegisterForm(Form):
    """user register form"""

    username = StringField(u"用户名", validators=[DataRequired(), Length(1, 30)])
    email = StringField(u"邮箱", validators=[DataRequired(), Email()])
    password = PasswordField(u"密码", validators=
                             [DataRequired(), equal_to("password2",
                                                       message=u"两次密码输入不同！")])
    password2 = PasswordField(u"确认密码", validators=[DataRequired()])
    submit = SubmitField(u"注册")


class UserForm(Form):
    """user profile detail form"""

    username = StringField(u"昵称", validators=[DataRequired(), Length(1, 30)])
    phone_number = IntegerField(u"电话号码", validators=[Regexp(
        r"^1(3|4|5|7|8)[0-9]\d{8}$", message=u"号码格式错误！")])
    about_me = StringField(u"一句话描述", validators=[Length(1, 100)])
    email = StringField(u"邮箱", validators=[Email()])
