#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

img_blueprint = Blueprint('img', __name__)

from . import views  # noqa
