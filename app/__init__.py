# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'app.config.DevelopmentConfig'))
db = SQLAlchemy(app)


from app.services import ScrapWeb, CollectionApi


@app.route('/')
def index():
    result = CollectionApi.get_list()
    title = 'Lista del osi'
    sub_title = 'La collección definitiva'
    return render_template('index.html', data=result, title=title, sub_title=sub_title)


@app.route('/check/<int:pk>', methods=['POST'])
def check(pk):
    result = CollectionApi.check_exist(pk)
    if result:
        pass
    return redirect(url_for('index'))


@app.route('/coleccion_list')
def api_list():
    result = CollectionApi.get_list()
    return jsonify(result), 200


@app.route('/scrap')
def scrap():
    ScrapWeb.save()
    return 'Hi!'


if(__name__ == 'app'):
    db.init_app(app)
    with app.app_context():
        db.create_all()
