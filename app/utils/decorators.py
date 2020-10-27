#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import redirect, url_for, abort
from functools import wraps
from . import request
import os


def session_required(func):
    """Checks whether user is logged in or redirect to login."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.get_login_user().get('u_id'):
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return wrapper


def public_page(func):
    """Checks whether user is logged in or redirect to login."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.get_login_user().get('u_id'):
            return redirect(url_for('index'))
        return func(*args, **kwargs)

    return wrapper


def private_request(func):
    """Checks if request contains valid security headers."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        u_id = request.get_header('u_id')
        if not u_id or u_id != os.environ.get("AUTH_HEADER"):
            return abort(401)
        return func(*args, **kwargs)

    return wrapper
