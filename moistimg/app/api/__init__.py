#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

from . import views  # noqa
