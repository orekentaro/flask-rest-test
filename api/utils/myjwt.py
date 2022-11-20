import time

from flask import json
from flask_jwt_extended import create_access_token
from models.user_master import UserMaster


def encode_jwt(user: UserMaster):
    payload_data = {
        "id": user.user_id,
        "auth": user.auth_id,
        "email": user.email,
    }
    return create_access_token(identity=json.dumps(payload_data), fresh=True)
