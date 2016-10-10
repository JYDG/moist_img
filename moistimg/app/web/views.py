#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils import secure_filename

from . import web_blueprint
from ..img.helpers import save_file


@web_blueprint.route('/')
def index():
    return render_template('web/index.html')


@web_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('web/upload.html')
    elif request.method == 'POST':
        file = request.files.get('upload_file')
        filename = secure_filename(file.filename)
        save_file(filename, file, current_app.config['FOLDERS']['upload'])
        return redirect(url_for('web.index'))
