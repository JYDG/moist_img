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
def run():
    app.run()

if __name__ == "__main__":
    manager.run()
