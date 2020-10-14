import os
from app.utils import const as CONST


class Config(object):
    FLASK_APP = "main.py"
    DEBUG = False
    TESTING = False
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    SCHEDULER_API_ENABLED = True


class Production(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
