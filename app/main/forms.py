#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from wtforms import Form, StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ProductForms(Form):
    """goods forms"""

    name = StringField(u"商品名", validators=[DataRequired()])
    category = StringField(u"选择种类", validators=[DataRequired()])
    introduction = TextAreaField(u"简介")
    submit = SubmitField(u"发布")
