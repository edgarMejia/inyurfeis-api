from flask import jsonify
from . import app
from .utils.decorators import private_request
import app.utils.const as CONST


@app.route(CONST.URL_INDEX, methods=["GET"])
@private_request
def index():
    return jsonify(success=True, message="/"), 200


@app.errorhandler(401)
def page_unauthorized(e):
    return jsonify(success=False, message="401 Unauthorized: Why are you here?"), 401


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(success=False, message="404 Not found"), 404
