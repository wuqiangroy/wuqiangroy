#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from .app import create_app, db
from flask_script import Manager

app = create_app(os.getenv("config") or "default")
manager = Manager(app)

if __name__ == "__main__":
    app.run()

