#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask.globals import request, session
import requests


def make():
    def get(url="", headers=""):
        return requests.get(url, headers=headers)

    def post(url="", headers=""):
        return requests.post(url, headers=headers)


def get_str(name):
    try:
        return request.values.get(name)
    except Exception as e:
        print("ERROR: request > get_str(param)", e)
        return ""


def get_int(name):
    try:
        return int(request.values.get(name))
    except Exception as e:
        print("ERROR: request > get_int(param)", e)
        return 0


def get_header(name):
    try:
        return request.headers.get(name)
    except Exception as e:
        print("ERROR: request > get_header(param)", e)
        return ""


"""
El manejo de las sesiones se hace desde aquí porque el contexto de la session solo se mantiene donde se manejan los
requests por lo que se hace aqui para poder acceder al objeto de la sesión desde cualquier otro modulo
"""


def get_login_user():
    return {
        "u_id": session.get('u_id'),
        "email": session.get('email'),
        "firstname": session.get('firstname'),
        "lastname": session.get('lastname'),
        "fullname": session.get('fullname')
    }


def set_login_user(id, email, firstname, lastname):
    session['u_id'] = id
    session['email'] = email
    session['firstname'] = firstname
    session['lastname'] = lastname
    session['fullname'] = f'{firstname} {lastname}'


def pop_session():
    session.pop('u_id', None)
    session.pop('email', None)
    session.pop('firstname', None)
    session.pop('lastname', None)
    session.pop('fullname', None)
