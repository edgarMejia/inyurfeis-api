#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import redirect, url_for
from functools import wraps
from . import request


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
