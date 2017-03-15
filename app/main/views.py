#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import request, jsonify, render_template, redirect, url_for
from flask_login import current_user
from app import db
from . import main
from .forms import ProductForms
from ..decorator import permission_required
from ..models import Goods


@main.route("/", methods=["GET", "POST"])
@main.route("/home/", methods=["GET", "POST"])
def index():
    return render_template("home.html")


@main("/sweet-grass/", methods=["GET", "POST"])
def sweet_grass():
    return render_template("sweet_grass.html")


@permission_required
@main.route("/publish-product/", methods=["GET", "POST"])
def publish_product():
    """publish goods"""

    form = ProductForms(request.args)
    if form.validate():
        goods = Goods(
            name=form.name.data.replace(" ", ""),
            pic=form.pic.data,
            category=form.category.data,
            introduction=form.introduction.data,
        )
        db.session.add(goods)
        db.session.commit()
        name = form.name.data.replace(" ", "")
        goods2 = Goods.query.filter_by(name=name).first()
        return redirect(url_for("main.goods", id=goods2.id))

    return render_template("publish_goods.html", form=form)


@main.route("/goods/<id>")
def goods_detail(id):
    """goods detail page"""
    goods = Goods.query.get_or_404(id)
    return render_template("goods.html", goods=goods)




