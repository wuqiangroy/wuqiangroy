#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Errors(object):
    """错误提示"""
    SUCCESS = 1200
    NO_DATA = 1001
    SERVER_ERROR = 1002
    # waiting for ......
    msg = {
        SUCCESS: u"成功",
        NO_DATA: u"未传递数据",
        SERVER_ERROR: u"服务器错误"
    }