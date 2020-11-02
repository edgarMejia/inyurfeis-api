#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from datetime import timedelta
from flask_bcrypt import Bcrypt
from .utils.decorators import session_required, private_request
from .utils.request import get_login_user
from .utils import const as CONST, json_encoder
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
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

    :return:
    """
    db.session.remove()


"""
Es necesario importar aquí para poder acceder a las rutas desde otros modulos
"""
# from . import routes
# from . import controllers
# from . import models
