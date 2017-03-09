#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from .app import create_app

app = create_app()

if __name__ == "__main__":
    app.run("localhost", port=8000, debug=True)

