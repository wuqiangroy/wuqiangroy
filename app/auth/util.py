#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import smtplib
import threading


class ThreadFun(threading.Thread):
    """执行多线程"""

    def __init__(self):
        super(ThreadFun, self).__init__()



class SendMail(object):
    """send mail server"""

