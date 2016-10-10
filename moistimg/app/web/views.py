#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template

from . import web_blueprint


@web_blueprint.route('/')
def index():
    return render_template('web/index.html')
