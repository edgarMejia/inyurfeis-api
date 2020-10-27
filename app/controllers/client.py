from flask import request, jsonify
from app import app, db
from app.utils.decorators import public_page
from app.models.client import Client


@app.route("/api/client/all", methods=["GET"])
@public_page
def get_all():
    data = []

    try:
        clients = Client.query.all()
        if clients:
            for client in clients:
                data.append(
                    dict(
                        id=client.id,
                        full_name=client.full_name,
                        auth_token=client.auth_token,
                        created_at=client.created_at
                    )
                )

        return jsonify(success=True, message="clients", data=data), 200
    except Exception as e:
        return jsonify(
            success=True,
            message="ERROR get all clients: " + str(e),
            data=data
        ), 400


@app.route("/api/client/save", methods=["POST"])
@public_page
def save():
    try:
        content = request.get_json()
    except Exception as e:
        print("ERROR: client > save()", e)
        return jsonify(success=False, message="No data", data=None), 400

    client = Client(content.get('full_name'), content.get('client_token'))

    try:
        db.session.add(client)
        db.session.commit()
        return jsonify(success=True, message="Client added"), 200
    except Exception as e:
        return jsonify(
            success=False,
            message="Error while adding new client: " + str(e),
            data=None
        ), 400
