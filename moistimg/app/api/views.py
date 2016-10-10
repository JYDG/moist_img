#!/usr/bin/python
# -*- coding:utf-8 -*-
from . import api_blueprint


@api_blueprint.route('/')
def index():
    return ''
