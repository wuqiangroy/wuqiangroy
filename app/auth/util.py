#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import threading

from flask import current_app, render_template
from flask_mail import Message
from .. import mail


class ThreadFun(object):
    """multi threading server"""

    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __call__(self):
        self.res = self.func(self.args)


def send_async_mail(app, msg):
    """multithreading send mail"""

    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    """send mail function"""

    app = current_app._get_current_object()
    msg = Message(app.config["MAIL_SUBJECT_PREFIX"]+" "+subject,
                  sender=app.config["MAIL_SENDER"], recipients=[to])
    msg.body = render_template(template+".txt", **kwargs)
    msg.html = render_template(template+".html", **kwargs)

    thr = threading.Thread(target=ThreadFun(send_async_mail, (app, msg)))
    thr.start()
    return thr



