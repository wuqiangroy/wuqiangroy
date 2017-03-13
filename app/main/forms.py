#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ProductForms(Form):
    """商品表单"""

    name = StringField(u"商品名", validators=[DataRequired()])
    category = SelectField(u"选择种类", coerce=int)
    introduction = TextAreaField(u"简介")
    submit = SubmitField(u"发布")
