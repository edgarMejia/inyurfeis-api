from flask import request, jsonify
from app import app, db
from app.utils.decorators import private_request
from app.utils.request import get_header
from app.models.logger import Logger


@app.route("/api/logger/<string:key>", methods=["POST"])
@private_request
def log_key(key=""):
    if not key:
        return jsonify(success=True, message="Empty key", data=None), 200

    logger = Logger(key, get_header('client_id'))

    try:
        db.session.add(logger)
        db.session.commit()
        return jsonify(success=True, message="Key added"), 200
    except Exception as e:
        return jsonify(
            success=False,
            message=f'Error while adding new key: ${str(e)}',
            data=None
        ), 400


@app.route("/api/logger/save", methods=["POST"])
@private_request
def logger_save():
    try:
        content = request.get_json()
    except Exception as e:
        print("ERROR: logger > save()", e)
        return jsonify(success=False, message="No data", data=None), 400

    logger = Logger(content.get('message'), content.get('client_id'))

    try:
        db.session.add(logger)
        db.session.commit()
        return jsonify(success=True, message="Log added"), 200
    except Exception as e:
        return jsonify(
            success=False,
            message="Error while adding new log: " + str(e),
            data=None
        ), 400
