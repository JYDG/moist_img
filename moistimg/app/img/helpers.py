#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

from flask import current_app


def is_allowed_extensions(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']


def save_file(filename, file, loc):
    file.save(os.path.join(loc, filename))


def check_and_make_dirs():
    for key, loc in current_app.config['FOLDERS'].items():
        if os.path.exists(loc):
            continue

        os.system("sudo mkdir {}".format(loc))
