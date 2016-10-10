#!/usr/bin/python
# -*- coding:utf-8 -*-
from . import img_blueprint


@img_blueprint.route('/')
def index():
    return ''
