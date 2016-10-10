#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from .web import web_blueprint
    app.register_blueprint(web_blueprint)
    return app
