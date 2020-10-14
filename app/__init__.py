#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from datetime import timedelta
from flask_bcrypt import Bcrypt
from .utils.decorators import session_required, public_page
from .utils.request import get_login_user
from .utils import const as CONST, json_encoder
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

"""Cambiar a CONST.PRODUCTION para cargar la configuración de producción"""
app.config.from_object(CONST.DEVELOPMENT)
app.json_encoder = json_encoder.JSONEncoder

bcrypt = Bcrypt(app)
app.permanent_session_lifetime = timedelta(hours=CONST.SESSION_LIFETIME_IN_HOURS)

db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    As in the declarative approach, you need to close the session after each
    request or application context shutdown.

    :param exception:
    :return:
    """
    db.session.remove()


@app.route(CONST.URL_INDEX, methods=["GET"])
@public_page
def index():
    return jsonify(success=True, message="/index"), 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(success=False, message="404 Not found"), 404


"""
Es necesario importar aquí para poder acceder a las rutas desde otros modulos
"""
from . import controllers
from . import models
