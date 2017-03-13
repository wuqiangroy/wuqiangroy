#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
from flask import request
from flask_login import current_user
from . import main
from .forms import ProductForms
from ..decorator import permission_required
from ..errors import Errors


@permission_required
@main.route("/publish-product/", methods=["GET", "POST"])
def publish_product():
    """发布商品"""

    form = ProductForms(request.args)
    if not form.validate():
        return Errors.NO_DATA, Errors.msg[Errors.NO_DATA]

    name = form.name.data.replace(" ", "")
    # category =
    introduction = form.introduction.data

    data = {
        "name": name,
        "category": None,
        "introduction": introduction
    }
    data = json.dumps(data)

    return Errors.SUCCESS, {'data': data}


