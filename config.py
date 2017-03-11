#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""配置"""

import os
import sys


class Config(object):
    SECRET_KEY = os.environ.get("secret_key") or "easy to guess secret key"

