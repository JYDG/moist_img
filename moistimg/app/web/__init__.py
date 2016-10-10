#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

web_blueprint = Blueprint('web', __name__)

from . import views