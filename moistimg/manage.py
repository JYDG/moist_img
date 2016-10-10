#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_script import Manager

# from werkzeug.contrib.fixers import ProxyFix

from app import create_app


app = create_app()
app.config.from_object('app.config')
# app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app)


@manager.command
def init():
    from app.img.helpers import check_and_make_dirs

    check_and_make_dirs()


@manager.command
def run():
    init()

    app.run(debug=True)

if __name__ == "__main__":
    manager.run()
