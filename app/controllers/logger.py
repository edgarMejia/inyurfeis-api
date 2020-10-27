from flask import request, jsonify
from app import app, db
from app.utils.decorators import private_request
from app.models.logger import Logger


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
